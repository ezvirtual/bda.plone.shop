Hannes Scratchpad
-----------------

    >>> [it[1].attrs['vendor_uid'] for it in soup.data.items()]
    >>> [it.attrs['order_uid'] for it in soup.query(Eq('creator', 'test'))]


unify naming
------------

    shop_uid -> vendor_area_uid (vendor_uid sounds better)

    is vendor really the right wording? -> (Vendor == Anbieter -> yup, klingt
    gut) then we need to rename vendor role to seller, since it's assigned
    individual sellers. -> vendor is OK
    vendors expect their area to be their shop, so ISubShop makes sense to me
    we've already discussed this. we stick to vendor now.


order view
----------

    calculate sums from allowed bookings


BUGS
====

- checkout - six payment - canceling six payment process with "back" button
  (some warnings are displayed by the browser...) -> the order is already
  stored! in that case, the order needs to be cleared.

  it is not a good idea to be too intelligent here. performing a shop order
  is a process done by a user which wants to buy something. issues like an
  aborted payment process or an error while sending email always needs manual
  investigation by either the shop owner, vendor or customer. never ever we
  want to delete an order by guessing - order states are the right way to
  handle edge cases -> an aborted payment process ends in an unpaid order which
  is completly fine.


TESTCASES
=========

- directly call @@checkout on item with empty cart -> redirect to item.
- anonymous @@checkout
- member @@checkout with @@personal-information filled out
- member @@checkout with no @@personal-information filled out

- create member, check if it's in Customer role


rnixx
-----

- darf anon benutzer einkaufen?
- darf anon benutzer preise sehen?


@@orders
--------

- perm. checks in code. eine view.
- req. parameter mit username.

- export auch angepasst

- enable vendor action

- vendor_uid ===> context uid ===> index in soup von booking.
        if no vendor set, use Plone Site uid /

- XXX: folder mit FTI vendor

- XXX: buyable uid


should orders be canceled on smtperrors?
----------------------------------------

2014-01-14 14:28:41 ERROR MailDataManager {'admin@admin.admin': (450, '4.1.2 <admin@admin.admin>: Recipient address rejected: Domain not found')}
Traceback (most recent call last):
  File "/home/thet-data/dotfiles-thet/home/.buildout/eggs/Products.CMFPlone-4.3.2-py2.7.egg/Products/CMFPlone/patches/sendmail.py", line 12, in _catch
    return func(*args, **kwargs)
  File "/home/thet-data/dotfiles-thet/home/.buildout/eggs/zope.sendmail-3.7.5-py2.7.egg/zope/sendmail/mailer.py", line 77, in send
    connection.sendmail(fromaddr, toaddrs, message)
  File "/usr/lib64/python2.7/smtplib.py", line 734, in sendmail
    raise SMTPRecipientsRefused(senderrs)
SMTPRecipientsRefused: {'admin@admin.admin': (450, '4.1.2 <admin@admin.admin>: Recipient address rejected: Domain not found')}

No, see explanation above


Mandantenfähigkeit
==================

- USt spezifika, nicht implementieren, ATM
  - über shop settings adapter...

- mandant soll nur für ihn bestimmte bestellungen sehen. wie?
  -> mandant sieht alle bestellungen in denen artikel aus seinem bereich liegen
  -> aber nur die buchungen die artikel des jeweiligen mandanten betreffen

  - mandanten spezifische shop einstellungen?
    -> später

  - mandant-typ? shop-typ?
    -> siehe oben -> vendor

  - mandant-permission auf context, alle bestellungen innerhalb dieses pfads?

- usecase - user bestellt bei verschiedenen mandanten.
  - unterschiedliche carts?
    -> nein, für den kunden ist das ganze portal ein einziger shop.
  - oder zusammengefasste bestellung?
    -> yup
