from configparser import ConfigParser 

def config(filename="database.ini", section="postgresql"):
    # create a parser, used to parse a config file
    parser = ConfigParser()
    # read the config file named database.ini. The config file consists of sections, each of which has a [section] header followed by name:value entries.
    parser.read(filename)
    db = {}
    if parser.has_section(section): # Search for the [postresql] section
        params = parser.items(section)
        for param in params: # Build up the db dict
            db[param[0]] = param[1]
    else:
        raise Exception('Section{0} is not found in the {1} file.'.format(section, filename))
    return db # db is a dict that looks something like: {'host': 'localhost', 'database': 'a3_q1', 'user': 'postgres', 'password': '56789'}