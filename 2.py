odd = list(range(1,10,2))  # [1,3,5,7]
backup= odd
odd = odd +[20]   # normal assign odd ra pak mikone va meghdar samte chap ra mirise dar odd
          # pas odd avaze mishe ama backup na
print(odd)
print(backup)
print('='* 40)

zoj = list(range(0,10,2))
backup2 =zoj
zoj += [20]    # augment assign zoj ra pak nemikone pas zoj va backup be 1 adres eshare mikonan
          # pas be har do adade 20 ezafe mishe
print(zoj)
print(backup2)
