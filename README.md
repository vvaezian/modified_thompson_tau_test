### Installation
```
pip install modified-thompson-tau-test
```
### Initialization
```python
from Modified_Thompson_Tau_Test.modified_thompson_tau_test import run_modified_thompson_tau_test
```
You can pass a list, a Pandas Series or a Pandas DataFrame to the function:
```python
run_modified_thompson_tau_test([2, 3, -50, 1, 0, 10, 1000])
```
The function returns the results as a Pandas DataFrame where the column `is_outlier` shows the result:
```
 	0 	is_outlier
2 	-50 	1
4 	0 	0
3 	1 	0
0 	2 	0
1 	3 	0
5 	10 	1
6 	1000 	1
```
