#regular expressions 
#import re
#pg = "Global warming is the hello F long-term1   increase 66 by Gloy hellooo error Error RROR is hellooooooo a ror of thor gror Shubham 3 in Ea$rth's average 5 Surface temperature, primarily Shiva caused by human activities that release greenhouse gases like carbon dioxide, methane, and nitrous oxide into the Globe a78tmosphere, Glowing which trap heat54 and intensify the natural green23house effect. Key drivers include the burning of fossil globe fuels for energy and transportation, deforestation, industrial processes, and certain agricultural practices. The consequences of this warming are far-reaching, with impacts ranging from rising sea levels and more frequent extreme weather events like heatwaves and floods to threats to ecosystems, ocean acidification, and significant economic disruptions. Addressing this crisis requires a global, concerted effort that includes transitioning to renewable energy, improving energy efficiency, protecting forests, and implementing policies to reduce emissions while also adapting to the changes already underway.The primary driver of global warming is the enhanced greenhouse effect, a natural process that is intensified by human activities. When humans burn fossil fuels such as coal, oil, and natural gas for power, transport, and industry, vast quantities of carbon dioxide are released into the atmosphere. Deforestation is another major contributor, as trees absorb from the atmosphere, and when they are cut or burned, this stored carbon is released, and the planet's ability to absorb future emissions is diminished. Other significant sources of greenhouse gases include agricultural activities, which release methane and nitrous oxide, and various industrial processes. These gases act like a blanket around the Earth, allowing sunlight in but trapping heat that would otherwise radiate back into space, causing the planet's average temperature to rise. Scientific evidence shows the Earth's average temperature has increased significantly since the pre-industrial era, with the rate of warming accelerating in recent decades.The impacts of this temperature increase are diverse and severe. One of the most visible effects is the melting of glaciers and polar ice caps, which contributes to a rise in sea levels, threatening coastal communities and low-lying island nations with inundation and increased storm surges. Changes in atmospheric and oceanic circulation patterns are leading to more frequent and intense extreme weather events, including hurricanes, heatwaves, droughts, and heavy rainfall. Ecosystems are also under immense pressure, with coral reefs experiencing bleaching due to warmer ocean temperatures and many species forced to migrate or face extinction as their habitats change. The oceans are absorbing excess, which is leading to ocean acidification, a process that harms marine life, particularly shelled organisms and coral reefs, and impacts fisheries.Economically, global warming poses substantial risks. The costs of responding to climate-related disasters, such as rebuilding infrastructure after floods and hurricanes, are significant. Furthermore, the impact on agriculture and water resources creates instability, while the overall costs of adapting to changing conditions and mitigating emissions are estimated to be in the trillions of dollars. However, investing in climate solutions also presents economic opportunities, such as job creation in the renewable energy sector and the development of a green economy.Addressing global warming is a complex challenge that requires action from governments, organizations, and individuals worldwide. At the international level, policies such as those outlined in the Paris Agreement are crucial for coordinating efforts to reduce emissions. Governments must implement regulations and incentives to promote a transition away from fossil fuels and toward renewable energy sources like solar and wind power. This also involves supporting research and development of new clean technologies. At the individual and community level, reducing one's carbon footprint through energy-efficient practices, using less fossil fuel, and making sustainable consumer choices can collectively make a difference.Ultimately, tackling global warming is not only an environmental imperative but also an economic and social one. By working together, societies can mitigate the worst effects of climate change and build a more sustainable and resilient future for generations to come. The urgency of the situation cannot be overstated, and immediate, concerted action is necessary to protect the planet"
#x = re.findall("[A-d]", pg)
#x = re.findall("\$", pg)
#x = re.findall("\s", pg)
#x = re.findall("\S", pg)
#x = re.findall("..ror", pg)
#x = re.findall("Gl.b..", pg)
#x = re.findall("^war", pg) - we'll catch up later
#x = re.findall("planet$", pg) # we'll catch up later
#x = re.findall("hel.o*", pg) #zero or more occurrences of preceding element
#x = re.findall("hel.o+", pg) #one or more occurrences of preceding element
#x = re.findall("hel.o{5}", pg) #exactly 5 occurrences of preceding element
#x = re.findall("hel.o{0,5}", pg) #between 0 and 5 occurrences of preceding element
#-------------------------------------------------- Set of sequences -------------------------------------
#x = re.findall("[au]", pg) #find all vowels
#print(x.count('a'))
#print(x.count('u'))
#x = re.findall("[A-Z]", pg) #find all alphabets
#x = re.findall("[^a-z,^0-9,^ ,^-]", pg) #negation - find all except small alphabets
#x = re.findall("[0-9]", pg) #find all alphanumeric characters
#x = re.search("Global", pg) #search function
#x = re.sub("\s", "7", pg, 5) #substitute function
#x = re.sub("\s", "7", pg)
#x = re.search("ra", pg)
#st = "Aakash Anand Ajay Bhanu Akash Amit Arjun" #by Raghav
#x = re.search(r"\bB\w+", st) #word boundary
#print(x)
#print(x.span())
#print(x.group())
#print(x.string)
#print(x[1]-x[0])
#txt = "The rain in Spain stays mainly in the plain be the sain coain"
#x = re.findall("[a-c]", txt)
#print(x)
