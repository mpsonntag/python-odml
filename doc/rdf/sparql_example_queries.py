from rdflib import Graph, RDF
from rdflib.plugins.sparql import prepareQuery

from odml.tools.rdf_converter import ODML_NS

rdf_namespace = {"odml": ODML_NS, "rdf": RDF}

resource = "./odml_RDF_example_A.ttl"

g = Graph()
g.parse(resource, format='turtle')
# select d.* from dataset d, stimulus s where s.contrast = '20%'
q1 = prepareQuery("""SELECT *
            WHERE {
               ?d rdf:type odml:Document .
               ?d odml:hasSection ?s .
               ?s rdf:type odml:Section .
               ?s odml:hasName "Stimulus" .
               ?s odml:hasProperty ?p .
               ?p odml:hasName "Contrast" .
               ?p odml:hasValue ?v .
               ?p odml:hasUnit "%" .
               ?v rdf:type rdf:Bag .
               ?v rdf:li "20.0" .
            }""", initNs=rdf_namespace)

g = Graph()
g.parse(resource, format='turtle')
# select d.* from dataset d, stimulus s, cell c where s.contrast = '20%' and c.celltype='P-unit'
q2 = prepareQuery("""SELECT *
                WHERE {
                   ?d rdf:type odml:Document .
                   ?d odml:hasSection ?s .
                   ?s rdf:type odml:Section .
                   ?s odml:hasName "Stimulus" .
                   ?s odml:hasProperty ?p .

                   ?p odml:hasName "Contrast" .
                   ?p odml:hasValue ?v .
                   ?p odml:hasUnit "%" .    
                   ?v rdf:type rdf:Bag .
                   ?v rdf:li "20.0" .


                   ?d odml:hasSection ?s1 .
                   ?s1 odml:hasName "Cell" .
                   ?s1 odml:hasProperty ?p1 .   

                   ?p1 odml:hasName "CellType" .
                   ?p1 odml:hasValue ?v1 .   
                   ?v1 rdf:li "P-unit" .                      
                }""", initNs=rdf_namespace)

# select d.* from dataset d, CellProperties s, EOD Frequency c where c.unit = 'Hz'
g = Graph()
g.parse(resource, format='turtle')
q3 = prepareQuery("""SELECT *
                WHERE {
                   ?d rdf:type odml:Document .
                   ?d odml:hasSection ?s .
                   ?s rdf:type odml:CellProperties .
                   ?s odml:hasProperty ?p .

                   ?p odml:hasName "EOD Frequency" .
                   ?p odml:hasValue ?v .
                   ?p odml:hasUnit "Hz" .    
                   ?v rdf:type rdf:Bag .
                   ?v rdf:li ?value .                      
                }""", initNs=rdf_namespace)

print("q1")
for row in g.query(q1):
    print("Doc: {0}, Sec: {1}, \n"
          "Prop: {2}, Bag: {3}".format(row.d, row.s, row.p, row.v))

print("q2")
for row in g.query(q2):
    print("Doc: {0}, Sec: {1}, \n"
          "Prop: {2}, Bag: {3}".format(row.d, row.s, row.p, row.v))
    print("Doc: {0}, Sec: {1}, \n"
          "Prop: {2}, Bag: {3}".format(row.d, row.s1, row.p1, row.v1))

print("q3")
for row in g.query(q3):
    print("Doc: {0}, Sec: {1}, \n"
          "Prop: {2}, Bag: {3} \n"
          "Value: {4}".format(row.d, row.s, row.p, row.v, row.value))
