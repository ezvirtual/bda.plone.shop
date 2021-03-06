from bda.plone.cart.interfaces import ICartItem
from bda.plone.orders.interfaces import IGlobalNotificationText
from bda.plone.orders.interfaces import IItemNotificationText
from bda.plone.orders.interfaces import IOrdersExtensionLayer
from bda.plone.shop import message_factory as _
from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.registry import DictRow
from plone.autoform.directives import widget
from plone.supermodel import model
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope import schema
from zope.interface import Interface
from zope.interface import provider


class IShopExtensionLayer(IOrdersExtensionLayer):
    """Browser layer for bda.plone.shop
    """


class IPotentiallyBuyable(Interface):
    """Mark item as potentially buyable.

    Considered for providing action in UI.
    """


class IBuyable(ICartItem):
    """Marker for buyable item.

    Item is buyable.
    """


class IShopSettingsProvider(Interface):
    """A marker interface for plone.registry configuration
    interfaces
    """


class IShopSettings(model.Schema):
    """Shop controlpanel schema.
    """

    admin_email = schema.ASCIILine(
        title=_(u"label_admin_email", default=u'Shop Admin E-Mail'),
        description=_(u"help_admin_email", default=u'No typos please....'),
        required=True,
        default=""
    )

    default_item_display_gross = schema.Bool(
        title=_(
            u'label_default_item_display_gross',
            default=u'Display Gross by default'
        ),
        required=False
    )

    currency = schema.Choice(
        title=_(u"label_currency", default="Currency"),
        description=_(
            u"help_currency",
            default=u"Choose the default currency"
        ),
        vocabulary='bda.plone.shop.vocabularies.AvailableCurrenciesVocabulary'
    )

    show_currency = schema.Choice(
        title=_(u"label_show_currency", default=u"Show the currency for items"),
        description=_(u"help_show_currency", default=u""),
        vocabulary=
            'bda.plone.shop.vocabularies.CurrencyDisplayOptionsVocabulary'
    )


@provider(IShopSettingsProvider)
class IShopCartSettings(model.Schema):
    """Shop controlpanel schema for cart settings.
    """

    model.fieldset(
        'cart',
        label=_(u'Cart'),
        fields=[
            'disable_max_article',
            'summary_total_only',
            'show_checkout',
            'show_to_cart',
        ],
    )

    disable_max_article = schema.Bool(
        title=_(u"label_disable_max_article", default=u"Disable max article"),
        description=_(
            u"help_disable_max_article",
            default=u"No total number of items in cart limit"
        ),
        default=True
    )

    summary_total_only = schema.Bool(
        title=_(
            u"label_summary_total_only",
            default=u"Cart Summary total only"
        ),
        description=_(
            u"help_summary_total_only",
            default=u"Show only total value in cart summary"
        ),
        default=False
    )

    show_checkout = schema.Bool(
        title=_(
            u"label_show_checkout",
            default=u"Show checkout link in portlet"
        ),
        description=_(u"help_show_checkout", default=""),
        default=False
    )

    show_to_cart = schema.Bool(
        title=_(
            u"label_show_to_cart",
            default=u"Show link to cart in portlet"
        ),
        description=_(u"help_show_to_cart", default=u""),
        default=True
    )


@provider(IShopSettingsProvider)
class IShopArticleSettings(model.Schema):
    """Shop controlpanel schema for article settings.
    """

    model.fieldset(
        'article',
        label=_(u'Article'),
        fields=[
            'quantity_units',
            'default_item_net',
            'default_item_quantity_unit',
            'default_item_comment_enabled',
            'default_item_comment_required',
            'default_item_quantity_unit_float',
        ],
    )

    widget('quantity_units', CheckBoxFieldWidget)
    quantity_units = schema.List(
        title=_(
            u"label_quantity_units",
            default=u"Specify quantity units allowed in shop."
        ),
        description=_(
            u"help_quantity_units",
            default=u'Quantity units (what the buyable items are measured in)'
        ),
        required=True,
        missing_value=set(),
        value_type=schema.Choice(
            vocabulary=
                'bda.plone.shop.vocabularies.AvailableQuantityUnitVocabulary'
        )
    )

    default_item_quantity_unit = schema.Choice(
        title=_(
            u"label_default_quantity_units",
            default=u"Specify default quantity name."
        ),
        description=_(
            u"help_default_quantity_unit",
            default=u'default measurement'
        ),
        vocabulary='bda.plone.shop.vocabularies.QuantityUnitVocabulary'
    )

    default_item_net = schema.Float(
        title=_(
            u'label_default_item_net',
            default=u'Default Item net price'
        ),
        required=False
    )

    default_item_comment_enabled = schema.Bool(
        title=_(
            u'label_default_item_comment_enabled',
            default='Comment enabled by default'
        ),
        required=False
    )

    default_item_comment_required = schema.Bool(
        title=_(
            u'label_default_item_comment_required',
            default='Comment required by default'
        ),
        required=False
    )

    default_item_quantity_unit_float = schema.Bool(
        title=_(
            u'label_default_item_quantity_unit_float',
            default='Quantity as float as default'
        ),
        required=False
    )


@provider(IShopSettingsProvider)
class IShopShippingSettings(model.Schema):
    """Shop controlpanel schema for article settings.
    """

    model.fieldset(
        'shipping',
        label=_(u'Shipping'),
        fields=[
            'include_shipping_costs',
            'shipping_method',
        ],
    )

    include_shipping_costs = schema.Bool(
        title=_(
            u"label_include_shipping_costs",
            default=u"Include Shipping Costs"
        ),
        description=_(u"help_include_shipping_costs", default=u""),
        default=True
    )

    shipping_method = schema.Choice(
        title=_(u"label_shipping_method", default=u"Shipping Method"),
        description=_(u"help_shipping_method", default=u""),
        vocabulary=
            'bda.plone.shop.vocabularies.AvailableShippingMethodsVocabulary'
    )


@provider(IShopSettingsProvider)
class IShopTaxSettings(model.Schema):
    """Shop controlpanel schema for tax settings.
    """

    model.fieldset(
        'tax',
        label=_(u'Tax Settings'),
        fields=[
            'vat',
            'default_item_vat',
        ],
    )

    widget('vat', CheckBoxFieldWidget)
    vat = schema.List(
        title=_(u"label_vat", default=u'VAT in %'),
        description=_(
            u"help_vat",
            default=u"Specify all allowed vat settings"
        ),
        required=True,
        missing_value=set(),
        value_type=schema.Choice(
            vocabulary='bda.plone.shop.vocabularies.AvailableVatVocabulary'
        )
    )

    default_item_vat = schema.Choice(
        title=_(u"label_default_vat", default=u'Default Value added tax name'),
        description=_(
            u"help_default_vat",
            default=u"Specify default vat name"
        ),
        vocabulary='bda.plone.shop.vocabularies.VatVocabulary'
    )


class ILanguageAwareTextRow(model.Schema):

    lang = schema.Choice(
        title=_(u'language', default=u'Language'),
        vocabulary='plone.app.vocabularies.SupportedContentLanguages',
        required=False
    )

    text = schema.Text(
        title=_(u'text', default=u'Text'),
        required=False
    )


@provider(IShopSettingsProvider)
class INotificationTextSettings(model.Schema,
                                IGlobalNotificationText,
                                IItemNotificationText):

    model.fieldset(
        'notifications',
        label=_(u'Notifications'),
        fields=[
            'global_order_text',
            'global_overbook_text',
            'order_text',
            'overbook_text',
        ],
    )

    widget('order_text', DataGridFieldFactory, auto_append=False)
    order_text = schema.List(
        title=_(
            u"label_order_notification_text",
            default=u"Per Item Order Notification Text"
        ),
        value_type=DictRow(
            title=_(u'order_text', default='Order Text'),
            schema=ILanguageAwareTextRow),
        required=False
    )

    widget('overbook_text', DataGridFieldFactory, auto_append=False)
    overbook_text = schema.List(
        title=_(
            u"label_overbook_notification_text",
            default=u"Per Item Overbook Notification Text"
        ),
        value_type=DictRow(
            title=_(u'overbook_text', default='Overbook Text'),
            schema=ILanguageAwareTextRow),
        required=False
    )

    widget('global_order_text', DataGridFieldFactory, auto_append=False)
    global_order_text = schema.List(
        title=_(
            u"label_overall_order_notification_text",
            default=u"Overall Order Notification Text"
        ),
        value_type=DictRow(
            title=_(u'order_text', default='Order Text'),
            schema=ILanguageAwareTextRow),
        required=False
    )

    widget('global_overbook_text', DataGridFieldFactory, auto_append=False)
    global_overbook_text = schema.List(
        title=_(
            u"label_overall overbook_notification_text",
            default=u"Overall Overbook Notification Text"
        ),
        value_type=DictRow(
            title=_(u'overbook_text', default='Overbook Text'),
            schema=ILanguageAwareTextRow),
        required=False
    )


class ILanguageAndPaymentAwareTextRow(model.Schema):

    payment = schema.Choice(
        title=_(u'payment', default=u'Payment'),
        vocabulary='bda.plone.shop.vocabularies.PaymentVocabulary',
        required=False
    )

    lang = schema.Choice(
        title=_(u'language', default=u'Language'),
        vocabulary='plone.app.vocabularies.SupportedContentLanguages',
        required=False
    )

    text = schema.Text(
        title=_(u'text', default=u'Text'),
        required=False
    )


@provider(IShopSettingsProvider)
class IPaymentTextSettings(model.Schema):

    model.fieldset(
        'payment',
        label=_(u'Payment'),
        fields=[
            'payment_text',
        ],
    )

    widget('payment_text', DataGridFieldFactory, auto_append=False)
    payment_text = schema.List(
        title=_(
            u"label_payment_text",
            default=u"Payment Texts"
        ),
        value_type=DictRow(
            title=_(u'payment_text', default='Payment Text'),
            schema=ILanguageAndPaymentAwareTextRow),
        required=False
    )
