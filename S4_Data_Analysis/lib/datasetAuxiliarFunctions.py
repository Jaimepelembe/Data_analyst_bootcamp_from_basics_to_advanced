# Auxiliar functions

def removeNullValues(dataset,column):
    """Removes the null values from a column of the dataset"""

    try:
        dataset=dataset.dropna(subset=[column])
    
    except KeyError as key:
        print(f"The column {column} doesn't exist in the dataset.")
    
    except NameError as ne:
        print(f"The dataset {dataset} doesn't exist.")

    except Exception as ex:
        print(ex)
    
    else:
        return dataset


def printRemotionNullValues(dataset,column):
    print(dataset[column].isnull().sum())
    dataset=removeNullValues(dataset,column)
    print(dataset[column].isnull().sum())
    return dataset



def removeOutliers(dataset,column):
    """Removes the outliers from a column of the dataset.
    
    Returns the dataset without outliers in the column
    """
    try:

        import numpy as np
        q1,q3 = np.percentile(dataset[column], [25,75])
        print(f" Q1 and Q3 = {q1} : {q3}" )
        
        iqr= q3 - q1
        lower = q1-1.5*iqr
        upper = q3+1.5*iqr
        print(f"Lower and upper = {lower} : {upper}")

        cleanDataset=dataset[ (dataset[column] >= lower) & (dataset[column]<=upper)]

    except KeyError as key:
        print(key)
    
    except NameError as ne:
        print(ne)
    except Exception as ex:
        print(ex)

    else:
        return cleanDataset


#removeOutliers(athletesDataset,"Weight")

#athletesDataset


def fillColumnMean(dataset,column,dtype=int):
    """Fill the NaN values of the Dataset with the mean value of the column.
    
    Parameters:

        dataset: The dataset.
        column: The column.
        dtype(int or float): The data type of the column.

    Returns:
        Dataset.
    """


    try:
        dataset[column]=dataset[column].fillna(dtype(dataset[column].mean()))
    
    except KeyError as key:
        print(f"The column {column} doesn't exist in the dataset.")
    
    except NameError as ne:
        print(f"The dataset {dataset} doesn't exist.")

    except Exception as ex:
        print(ex)
    
    else:
        return dataset