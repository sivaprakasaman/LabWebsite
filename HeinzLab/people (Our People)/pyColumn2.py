email = person.get('email','')
phone = person.get('office_phone','')
office = person.get('office','')

if email:
  print '<div class="people-list-email"><a href="mailto:%s">%s</a></div>' % (email, email)

if phone:
  print '<div class="people-list-phone">%s</div>' % container.ResourceDB.Templates.pyFmtPhone(phone, bold_digits=0)

if office:
  print '<div class="people-list-office">%s</div>' % (office)

return printed
