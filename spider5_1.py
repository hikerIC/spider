#import logging
from scrapy.selector import Selector
with open('./superHero.xml') as fp:
    body = fp.read()

print(Selector(text=body).css('class name').extract())
for i, x in enumerate(Selector(text=body).xpath('//name[@lang="en"]').extract()):
    print(i, x)
print(Selector(text=body).xpath('/html/body/superhero/class[last()-1]/name/text()').extract())

