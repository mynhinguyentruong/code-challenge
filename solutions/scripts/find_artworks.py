from lxml.html import parse
import pprint
import json

name = input("Enter desire name of output json file: ")


artworks = []

def extract_artworks_info(path_to_file, art_work_div_classname, img_attribute_name, div_classname_with_name, div_classname_with_extensions):
    artworks_info = []

    # Read HTML content from the file
    with open(path_to_file, "r", encoding="utf-8") as file:

    # Parse the html file
        doc = parse(file).getroot()

        # Find the div with art_work_div_classname
        artworks_list = doc.find_class(art_work_div_classname)

        # Extract information from each artwork
        for artwork in artworks_list:
            obj = {}

            # Grab the <a>
            link = list(artwork.iterlinks())

            # Get the href attribute
            (element, attribute, link, pos) = link[0] 

            # Grab the <img> and get src attribute
            img_src = artwork.cssselect("img")[0].get(img_attribute_name)

            obj["name"] = artwork.find_class(div_classname_with_name)[0].text_content() 
            obj["link"] = "https://www.google.com" + link

            if artwork.find_class(div_classname_with_extensions):
                obj["extensions"] = [artwork.find_class(div_classname_with_extensions)[0].text_content()]

            obj["image"] = img_src 
            print(obj["name"])

            artworks_info.append(obj)

    # Log result to terminal
    pp = pprint.PrettyPrinter(depth=4)
    pp.pprint(artworks_info)

    # Write to .json
    result = {"artworks": artworks_info}
    with open("./jsons/" + name + ".json", "w") as outfile: 
        json.dump(result, outfile)

    return artworks_info

extract_artworks_info("./static-html/pablo_paintings.html", "iELo6", "src", "pgNMRc", "cxzHyb" )



