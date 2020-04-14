if not phone:
  return ''

phones = []
formatted = []

if same_type(phone, 0):
  phone = str(phone)

if not same_type(phone, ''):
  person = phone
  phones.append(str(person.office_phone))
  if person.other_phone:
    phones.append(str(person.other_phone))
else:
  phones.append(str(phone))

for phone_num in phones:
  number = ''
  paren_string = ''
  in_parens = 0
  has_chars = 0
  paren_strings = []

  for c in phone_num:
    if c in string.digits:
      number = number + c
    if in_parens and c != ')':
      if c in string.letters:
        has_chars = 1
      paren_string = paren_string + c
    if c == '(':
      in_parens = 1
      has_chars = 0
      paren_string = ''
    if c == ')':
      in_parens = 0
      if has_chars:
        paren_strings.append(str(paren_string) + ' - ')    

  if len(number) == 10:
    pass
  elif len(number) == 5:
    number = '76549' + number
  elif len(number) == 7:
    number = '765' + number 
  elif len(number) >= 11 and number[0] == '1':
    number = number[1:]

  this_number = "(%s) %s-%s" % (number[0:3], number[3:6], number[6:10])

  if bold_digits > 4:
    bold_digits = min(bold_digits, 7)
    digits = bold_digits + 1
    this_number = this_number[:-digits] + '<strong>' + this_number[-digits:] + '</strong>'

  if len(number) == 10:
    formatted.append("%s%s" % (' '.join(paren_strings), this_number))
  elif len(number) > 14:
    formatted.append("%s%s, %s" % (' '.join(paren_strings), this_number, container.pyFormatPhone(number[10:], bold_digits)))
  elif len(number) > 10:
    formatted.append("%s%s x%s" % (' '.join(paren_strings), this_number, number[10:]))
  else:
    formatted.append(str(phone))

return '<br />'.join(formatted)
