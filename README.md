# Big-Mart-Sales-Prediction

## Sales Prediction for Big Mart Outlets

The data scientists at BigMart have collected 2013 sales data for 1559 products across 10 stores in different cities. Also, certain attributes of each product and store have been defined. The aim is to build a predictive model and predict the sales of each product at a particular outlet.

Using this model, BigMart will try to understand the properties of products and outlets which play a key role in increasing sales.

Please note that the data may have missing values as some stores might not report all the data due to technical glitches. Hence, it will be required to treat them accordingly. 

## Data Dictionary

We have train (8523) and test (5681) data set, train data set has both input and output variable(s). You need to predict the sales for test data set.


**Train file:** CSV containing the item outlet information with sales value:-

|Variable|	Description|
|---------|------------|
|Item_Identifier	|Unique product ID||
|Item_Weight|	Weight of product|
|Item_Fat_Content	|Whether the product is low fat or not|
|Item_Visibility|	The % of total display area of all products in a store allocated to the particular product|
|Item_Type|	The category to which the product belongs|
|Item_MRP|	Maximum Retail Price (list price) of the product|
|Outlet_Identifier	|Unique store ID|
|Outlet_Establishment_Year|	The year in which store was established|
|Outlet_Size|	The size of the store in terms of ground area covered|
|Outlet_Location_Type	|The type of city in which the store is located|
|Outlet_Type|	Whether the outlet is just a grocery store or some sort of supermarket|
|Item_Outlet_Sales	|Sales of the product in the particular store. This is the outcome variable to be predicted.|

**Test file:** CSV containing item outlet combinations for which sales need to be forecasted

|Variable|	Description|
|---------|------------|
|Item_Identifier|	Unique product ID|
|Item_Weight	|Weight of product
Item_Fat_Content	|Whether the product is low fat or not|
|Item_Visibility|	The % of total display area of all products in a store allocated to the particular product|
|Item_Type	|The category to which the product belongs|
|Item_MRP	|Maximum Retail Price (list price) of the product|
|Outlet_Identifier	|Unique store ID|
|Outlet_Establishment_Year|	The year in which store was established|
|Outlet_Size	|The size of the store in terms of ground area covered|
|Outlet_Location_Type	|The type of city in which the store is located|
|Outlet_Type|	Whether the outlet is just a grocery store or some sort of supermarket|

## Feature Discription:-

- **Item_Identifier**:- This feature contains 1559 unique items that is being sell from different outlet
- **Item_Weight**:- This feature contains the weight of different Items and the range of the weight vary from 4.5  to 21.3 and every Item has same weight through out the dataset, also there is 1463 null value in this column
- **Item_Fat_Content**:- This feature contains 5 different categories namely "Low Fat" , "Regular", "LF" , "low fat", and "reg", but there are actually 2 categories that is "Low Fat" and "Regular"
- **Item_Visibility**:- The % of total display area of all products in a store allocated to the particular product
- **Item_Type**:- This feature has 16 categories in it.
- **Item_MRP**:- This feature contents the MRP of the item which vary from 31.29 to 266.88 
- **Outlet_Identifier**:- This feature contains 10 different categories, that means there are 10 outlets in the dataset.
- **Outlet_Establishment_Year**:- This feature contains the year in which the outlet is estabilished, it contains 9 unique year in which the outlets are established, In the year of 1985 there is two outlets established namely "OUT027" and "OUT019" which is also the oldest in the dataset and the latest one is established in 2009
- **Outlet_Size**:- This feature contains 3 different categories which is size of the outlets, also has 2410 null value in it. outlet "OUT045", "OUT017" and "OUT010" has not cateories in any of the "Outlet_Size" category
- **Outlet_Location_Type**:- This feature has 3 categories namely "Tier1" ,"Tier2" and "Tier3".
- **Outlet_Type**:- This feature  has 4 categories namely "Supermarket Type1" , "Supermarket Type2", "Supermarket Type3" and "Grocery Store"