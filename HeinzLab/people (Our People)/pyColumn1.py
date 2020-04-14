if not group_id:
  group_id = container.plPrimaryGroupId

name = container.pyFmtName(person)
resource_id = person.get('resource_id','')
title = person.get('title','')
bio = person.get('bio','')
root = container.getRoot()

url = '%s/ptProfile?resource_id=%s&group_id=%s' % (container.absolute_url(), resource_id, group_id)

print '<a href="%s">%s</a>' % (url, name)

if title:
  print '<div class="people-list-title">%s</div>' % title
  
if show_bio and bio:
  print '<div class="people-list-bio">%s</div>' % root.ResourceDB.pyFmtNewlineToBR(bio)

return printed
