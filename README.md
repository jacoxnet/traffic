# Project 5 in CS50x AI

## Traffic

This program calls the tensorflow library to construct a neural network to recognize
signs from the German Traffic Recognition Benchmark 
[GTSRB](http://benchmark.ini.rub.de/?section=gtsrb&subsection=newsdataset)

The GTSRB data is stored in a subdirectory of the main `traffic` directory. When called with
`python3 traffic.py gtsrb`, the program:

- reads in the dataset
- creates a model using tensorflow
- trains the model on a portion of the data and then tests its accuracy on the rest.

### Experimentation

I started with the same layers and in the same order as the model used in the handwriting 
example in class, modified for the shape of the input and the size of the necessary
output. That produced a poor (5%) recognition rate on this dataset. I made the following 
experimental modifications that had a significant effect on accuracy:

- lowered the dropout rate from 0.5 to 0.2 (improved test data accuracy to 79%)
- added a second convolution and pooling layer similar to the first (improved accuracy to 95%)
- increased the recognition units from 128 to 256

Then I made some more changes that had a minimal or slightly harmful effect:

- adding third convolution-pooling layer
- enlarging kernel in first convolution 

The final result produced accuracy numbers that ranged fromr 94% - 96%.


