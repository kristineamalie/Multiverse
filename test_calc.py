'''Author: Kristine Petersen. 
This programme tests the iris app Version: 1.0
'''


from calc import predict_species

def testing_max_values():
    #establish input values
    
    sepal_length = 8.0
    sepal_width = 4.5
    petal_length = 7.0
    petal_width = 2.7
# calculate an output
    species = predict_species(sepal_length, sepal_width, petal_length, petal_width)
    assert species == 'virginica'
    

def testing_first_value():
        #establish input values
        
        sepal_length = 5.1
        sepal_width = 3.5
        petal_length = 1.4
        petal_width = 0.2
    # calculate an output
        species = predict_species(sepal_length, sepal_width, petal_length, petal_width)
        assert species == 'setosa'

def testing_avreage_flower():
    #see how to get average numbers for each species and see if that works
    
    sepal_length = 5.936
    sepal_width = 2.770
    petal_length = 4.260
    petal_width = 1.326
# calculate an output
    species = predict_species(sepal_length, sepal_width, petal_length, petal_width)
    assert species == 'versicolor'
        
        
def test_string():
        #testing that the output is string
    species = predict_species(4, 1.8, 8.5, 4.1)
    assert isinstance(species, str)