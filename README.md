# Creating Living Documentation with Odoo and Behave
This repo contains demo code that accompanies my talk at Odoo Experience 2015. To run the example you'll need to add my
[fork of Behave](https://github.com/Gimpneek/behave "My Fork of Behave") (pull request on it's way) and run Behave from the repo folder like you would normally with OERPScenario.

`behave --livingdoc --livingdoc-directory=living_doc --livingdoc-meta=livingdoc_config.json /path/to/features/`

## Demo
[Living Documentation for this project](http://gimpneek.github.io/odoo_living_documentation_demo/living_doc/index.html "Living Documentation for this project")

## Installing the modified Behave
Remove your existing Behave and run (may require sudo):
`pip install git+https://github.com/Gimpneek/behave.git`

## Demo data used with the tests
You'll need to create a new database with demo data. I'm using a few demo users for testing the assign and review tasks, all just need a name and project user rights:
- Colin
- Joel
- Lorenzo
- Will
- Julian
- Eckhard
- Rob

## Hat tips
- [OERPScenario](https://github.com/camptocamp/oerpscenario "OERPScenario")
- [Behave](https://github.com/behave/behave/ "Behave")
- [Specification by Example](http://specificationbyexample.com/ "Specification by Example")

## Get in touch
- [@colinwren](https://twitter.com/colinwren "@colinwren")
- colin@neovahealth.co.uk
