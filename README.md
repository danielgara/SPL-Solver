
## XCSP3

XCSP3 is an XML-based format designed to represent instances of combinatorial constrained problems from the angle of Constraint Programming (CP). 
XCSP3 is an intermediate integrated format that can represent each instance separately while preserving its structure. 
For only dealing with the most popular constraints and frameworks, use XCSP3-core. 
For modeling problems declaratively, and compiling them into XCSP3 instances, use the new Java-based API MCSP3.

## Feature Model

In software development, a feature model is a compact representation of all the products of the Software Product Line (SPL) in terms of "features". Feature models are visually represented by means of feature diagrams. Feature models are widely used during the whole product line development process and are commonly used as input to produce other assets such as documents, architecture definition, or pieces of code.

## VariaMos

A product line tool for variability modeling and reasoning. 

VariaMos Web was designed as a modeling tool which incorporates different modeling languages to specify and analyze families of systems, for instance (self) adaptive systems and (dynamic) product lines supporting several types of models and frameworks in a graphically-oriented application available from any web browser.

VariaMos is suppose to be a new way to model the life cycle of (dynamic) product lines and families of systems, through the use of a high level constraint language to represent and reason over different models by means of different solvers (e.g., GNU and SWI Prolog). 

### Feature Model in VariaMos

The VariaMos APP creates the feature models using MxGraph, this library creates models via an XML representation, the idea is to translate such XML to XSCP3 format.

MxGraph is a fully client side JavaScript diagramming library that uses SVG and HTML for rendering. draw.io is an example that extends the functionality of this library. The sources to draw.io are also available.

## The Algorithm

1) Open the MxGraph file
2) Search XPath for root and concrete tags and create a list with this tags
3) Exclude MXGraph default root node and duplicated concrete tags
4) Transform the matched tags into a set of features
5) Search XPath for rel_concrete_root, rel_abstract_root, rel_concrete_abstract and rel_concrete_concrete tags
6) Create a list of relations with type of the relation and relation id
7) Iterate over the feature list creating XSCP3 variables <var id={id}> 0 1 </var>
8) Iterate over the list of relations creating constrains depending of the relation type
8.1) eq(var, 1) for the root
8.2) eq(father, child) for the mandatory relation
8.3) ge(father, child) for the optional relation
8.4) gt(add(sub(1, child), father), 0) for the requires relation
8.5) gt(add(sub(1, child), sub(1, father)), 0) for the excludes relation

