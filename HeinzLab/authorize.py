request = context.REQUEST
qualified_name = directory['qualified_name']

roles = []

# To add additional Roles create a new Persistent List
# object in the same folder as this authorize script.
# Within this script create a new block in the format:
#
# try:
#   if qualified_name in container.persistentList():
#     roles.append('NewRole')
# except:
#   pass
#
# A blocks has been created for Manager.

try:
  if qualified_name in container.authorizeManagers():
    roles.append('Manager')
except:
  pass

return roles
