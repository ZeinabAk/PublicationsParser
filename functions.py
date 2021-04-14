import copy
from scholarly.data_types import Author, AuthorSource, Publication, PublicationSource
from scholarly import scholarly
import pprint
def printS(self):
    """Pretty print an Author or Publication container object

    :param object: Publication or Author container object
    :type object: Author or Publication
    """
    if 'container_type' not in self:
        print("Not a scholarly container object")
        return

    to_print = copy.deepcopy(self)
    if to_print['container_type'] == 'Publication':
        to_print['source'] = PublicationSource(to_print['source']).name
    elif to_print['container_type'] == 'Author':
        parser = AuthorParser(self.__nav)
        to_print['source'] = AuthorSource(to_print['source']).name
        if parser._sections == to_print['filled']:
            to_print['filled'] = True
        else:
            to_print['filled'] = False

        if 'coauthors' in to_print:
            for coauthor in to_print['coauthors']:
                coauthor['filled'] = False
                del coauthor['container_type']
                coauthor['source'] = AuthorSource(coauthor['source']).name

        if 'publications' in to_print:
            for publication in to_print['publications']:
                publication['source'] = PublicationSource(publication['source']).name
                del publication['container_type']

    del to_print['container_type']
    return pprint.pformat(to_print)