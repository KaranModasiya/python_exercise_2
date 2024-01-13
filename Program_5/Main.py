from xml.dom.minidom import parse

file = parse('data.xml')

template = file.getElementsByTagName('template')
print(list(map(lambda x: x.getAttribute('id'), template)))
# print([x.getAttribute('id') for x in template])

xpath = file.getElementsByTagName('xpath')
print(list(map(lambda x: x.getAttribute('position'), xpath)))
# print([x.getAttribute('position') for x in xpath])

link = file.getElementsByTagName('link')
print(list(map(lambda x: x.getAttribute('href').split('/')[-1], link)))
# print([x.getAttribute('href') for x in link])

script = file.getElementsByTagName('script')
print(list(map(lambda x: x.getAttribute('src').split('/')[-1], script)))
# print([x.getAttribute('src') for x in script])

