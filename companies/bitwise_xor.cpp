Recently, Bob read an article about bitwise operations. He came up with a problem and gave it to Alice to solve. However, Alice is busy doing some work, hence solve the following problem for her.

You have an array of integers (initially empty).

You are also given an array type where typei denotes the type of the ith query and array X where Xi denotes the parameter of the ith query

You have to perform Q queries on this array. Each query belongs to one of three types:

type 1: &quot;1 X&quot; — Add the element X to the array
type 2: &quot;2 X&quot; — Delete all the occurrences of X in the array
type 3: &quot;3 X&quot; — Print the sum of all the elements currently present in the array by taking bitwise XOR with X, i.e. , where N is the length of the current array.

Task

Determine the required sum for each query of type 3.

Notes

 : Denotes the bitwise XOR operator
For a query of type 3, you are not actually taking bitwise XOR with X i.e. the array remains unchanged after the query
It is guaranteed that there will be at least one query of type 3
Output 0 if the array is empty while performing a query of type 3.

Examples

Assumptions

Q = 7
type = [1, 1, 1, 2, 1, 3, 3 ]
X = [5, 5, 11, 5, 16, 7, 11]

Approach

There are 7 queries. Let our array be A = [ ]  (initially empty).

Query 1: type 1 — add 5 to A, A = [ 5 ]
Query 2: type 1 — add 5 to A, A = [ 5, 5]
Query 3: type 1 — add 11 to A, A = [ 5, 5, 11]
Query 4: type 2 — delete all the occurrences of 5, A = [ 11 ]
Query 5: type 1 — add 16 to A, A = [ 11, 16 ]
Query 6: type 3 —  add 35 to the output array

Query 7: type 3 — , add 27 to the output array

Hence the output for the queries is [35, 27]

Function description

Complete the function solve() provided in the editor. This function takes the following 3 parameters and returns the output_array containing answers to each query of type 3:

Q: Represents the size of the arrays, respectively type and X
type: Represents the type of the ith query
X: Represents the parameter of the ith query

Input format

The first line contains T denoting the number of test cases. T also specifies the number of times you have to run the solve() function on a different set of inputs.
For each test case:
The first line contains Q denoting the size of arrays type and X.
The second line contains space-separated values in the range 1 to 3, denoting the type of each query.
The third line contains space-separated values in the range 0 to 109, denoting the parameter of each query.

Output format For each test case in a new line, output the required sum for each query of type 3.

Constraints

 .

Code snippets (also called starter code/boilerplate code)

This question has code snippets for C, CPP, Java, and Python.


#include<bits/stdc++.h>
using namespace std;

int q_sum = 0;
vector<long long> solve (int Q, vector<int> type, vector<int> X) {

    vector < long long > output_array;
    map < long long, long long> freq;
    long long curr_size = 0;

    vector<long long> set_bits(32, 0LL);
    vector<long long> power2(32, 0LL);
    power2[0] = 1;

    for (int i = 1; i< 32; i++) power2[i] = power2[i-1]*2LL;

    for (int i = 0; i< Q; i ++){
        int typ = type[i];
        if (typ ==1){
            long long x=X[i];
            for (int j = 0; j<32; j++){
                set_bits[j] += (x%2);
                x /= 2;
            }
            curr_size++;
            freq[X[i]]++;

        } else if (typ == 2){
            long long x = X[i];
            for(int j = 0; j< 32; j++){
                set_bits[j] -= freq[X[i]]*(x%2);
                x/=2;
            }
            curr_size -= freq[X[i]];
            freq[X[i]] = 0;
        } else {
            if (curr_size == 0) {
                output_array.push_back(0);
                continue;
            }

            long long out = 0LL;
            long long x = X[i];

            for (int j = 0; j <32; j++) {
                int bt = x%2;
                x/= 2;
                if(bt) out  += (curr_size - set_bits[j])*power2[j];
                else out += (set_bits[j])*power2[j];
            }
            output_array.push_back(out);
        }
    }
    return output_array;
   
}

int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for(int t_i = 0; t_i < T; t_i++)
    {
        int Q;
        cin >> Q;
        vector<int> type(Q);
        for(int i_type = 0; i_type < Q; i_type++)
        {
        	cin >> type[i_type];
        }
        vector<int> X(Q);
        for(int i_X = 0; i_X < Q; i_X++)
        {
        	cin >> X[i_X];
        }

        vector<long long> out_;
        out_ = solve(Q, type, X);
        cout << out_[0];
        for(int i_out_ = 1; i_out_ < out_.size(); i_out_++)
        {
        	cout << " " << out_[i_out_];
        }
        cout << "\n";
    }
}