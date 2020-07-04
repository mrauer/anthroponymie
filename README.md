# Anthroponymie

* Get the file from Insee.
* Each first name is a unique set. (33,484 distincts).
* Get a subset of first name based on cutoff. (ex: 85% of population).
* Process one letter at the time. (ex: M).
* Create pickled dict in data/, empty when initiated (M_85.dat).
* Store URLs in Mongo, and proceed one at the time to extract birthplace.
* Ex: {"laurent":{"france":81, "spain":2, "switzerland":23}}
