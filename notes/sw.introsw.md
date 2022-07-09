---
id: n6h4fv35x31yav1tqhtub7n
title: Introduction to the Semantic web
desc: ''
updated: 1655825000758
created: 1655461752331
---
## Introduction to the Semantic web

## What are its semantics?

- Semantics is meaning of word, phrase, or text.
- Semantics is description
- Semantics is metadata = data about data

## Semantic Web: Why

- Task require combining data across the internet
- Human understand how to combine this information
- Machines aren't smart enough

## Ways to Enable Machine Processing

![Enable Machine Processing](/assets/images/2022-06-17-17-49-49.png)

- Smarter Machines &rarr; AI/ML/NLP
- Smarter Data &rarr; Semantic Web &rarr; Standard
machine-readable format

## Semantic Web: A Web of Data

## The Semantic Web Technology Stack

![semantic stack](/assets/images/2022-06-17-17-53-52.png)

> Machine-processable data

Smart data approach

- Semantics is made explicit by formal(structured) and standardized knowledge representation (Ontology) can be KG, Linked data
- It will be possible:
  - to process the meaning of information automatically
  - to relate and integrate heterogeneous data (different website/source)
  - to deduce implicit (not evident) information from existing (evident) information in an automated way
- The Semantic Web is kind of a global database that contains a universal network of semantic proposition

## Semantic Web Architecture

![semantic web technology stack](/assets/images/2022-06-19-21-46-45.png)

- **Unicode** is a standard of encoding international character sets and it allows that all human languages can be used.
- **Uniform Resource Identifier (URI)** is a string of a standardized form that allows to uniquely identify resources (e.g., documents).
  - A subset of URI is Uniform Resource Locator (URL), which contains access mechanism and a (network) location of a document - such as <http://www.example.org/>.
- **Extensible Markup Language (XML)** **Generalization of HTML** **Self-describing documents** is a general purpose markup language for documents containing structured information. A XML document contains elements that can be nested and that may have attributes and content.
- A core data representation format for semantic web is **Resource Description Framework (RDF)** **Graph Model**. RDF is a framework for representing information about resources in a graph form. It was primarily intended for representing metadata about WWW resources, such as the title, author, and modification date of a Web page, but it can be used for storing any other data. It is based on triples subject-predicate-object that form graph of data. All data in the semantic web use RDF as the primary representation language.
- To allow standardized description of taxonomies and other ontological constructs, a RDF Schema (RDFS) was created together with its formal semantics within RDF. RDFS can be used to describe taxonomies of classes and properties and use them to create lightweight ontologies.
- More detailed ontologies can be created with Web Ontology Language OWL. The OWL is a language derived from description logics, and offers more constructs over RDFS. It is syntactically embedded into RDF, so like RDFS, it provides additional standardized vocabulary.
- Rule languages are being standardized for the semantic web as well. Two standards are emerging - RIF andSWRL.
- For querying RDF data as well as RDFS and OWL ontologies with knowledge bases, a **Simple Protocol and RDF Query Language (SPARQL)** is available. SPARQL is SQL-like language, but uses RDF triples and resources for both matching part of the query and for returning results of the query.
- Formal proof together with trusted inputs for the proof will mean that the results can be trusted. For reliable inputs, cryptography means are to be used, such as digital signatures for verification of the origin of the sources.
- On top of these layers, application with user interface can be built.

## References and Resources

- Marek Obitko: Semantic Web Architecture
(<https://www.obitko.com/tutorials/ontologies-semantic-web/semantic-web-architecture.html>)
- Rhys Lewis: Dereferencing HTTP URIs (<http://www.w3.org/2001/tag/doc/httpRange-14/2007-05-31/HttpRange-14>)

## REPRESENTING KNOWLEDGE ON THE WEB

## Knowledge Representation

- Structure data
- Formal Representation
- Machine-Readable
- Machine-Understable
- Machine-Processable

![example](/assets/images/2022-06-19-21-58-57.png)

## UML instance

```UML
Pluto: Planet
discovered: 1930
```

## HTML

```HTML
<a href="http://en.wikipedia.org/wiki/Pluto">Pluto</a> has been discovered in 1930.
```

## XML

```XML
<planet name = "Pluto" discovered= "1930" />
```

![xml](/assets/images/2022-06-19-22-08-31.png)

### XML Schema A

```XML
<discovered>
  <discovery>Pluto</discovery>
  <year>1930</year>
</discovered>
```

### XSLT Transformation

```XML
<xsl:stylesheet version="1.0" xmlns:xsl="http://....Transform">
  <xsl:template match="/">
  ....
  </xsl:template>
</xsl:stylesheet>
```

### XML Schema B

```XML
<planet name = "Pluto" discovered= "1930" />
```

## RDF : Represented as an RDF Graph or Knowledge Graph

![rdf](/assets/images/2022-06-19-22-13-02.png)

![node](/assets/images/2022-06-19-22-14-53.png)

## RDF: Resource Description Framework

> - A language for representing information about resources in the World Wide Web
>
> - RDF can also be used to represent information about things that can be identified on the Web, even when they cannot be directly retrieved on the Web

- Resource
  - can be everything on the web
  - must be uniquely identified and referenceable via URI
- Description
  - =description of resources
  - via representing properties and relationships among resources as graphs
- Framework
  - = combination of web based protocols (URI, HTTP, XML, Turtle, JSON, ....)
  - based on formal model (semantics)
- Knowledge in RDF is expressed as a list of statements
- all RDF statements follow the same simple schema (= RDF Triple)

![rdf](/assets/images/2022-06-19-22-22-54.png)

W3C standard (Primer: <http://www.w3.org/TR/rdfprimer/>)
