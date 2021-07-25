#include "iostream"
#include "vector"
using namespace std;
// This is the Function make to sort the time on the basis of end date 
bool check ( vector<int> a , vector<int> b){
  return a[1]<b[1];
}

int main(){
  int n ;
  cin >> n;
  // Create a vector of vector storing integers
vector <vector <int> > d;
// Taking in input as first the row get selected for input and then respective columns are filled
for(int i=0;  i < n ;  i++){ 
    vector <int> row;
    for(int j=0 ;  j<2; j++){
      int temp ;
      cin>>temp;
      // Add element to the column
      row.push_back(temp);
    }
    // Add a whole Row 
    d.push_back(row);
}
// Sorting is called row wise . So for each row we can check their second element 
sort(d.begin() , d.end()  , check);

// Logic Can Be Like If we sort all the task by endtime so a task could be picked up only if the starting time of task is greater or equal to ending time of previous task . So we would get maximum task done as the task needs to be finished before next one to get started.

int end  = 0 ;
for(int i=0 ; i< n ; i++){
  if(end <= d[i][0]){
    end = d[i][1];
    cout << i << " ";
  }
}

// for(int i = 0 ; i< n ; i++){
//   cout<<d[i][0]<<" "<<d[i][1]<<endl;
// }

}
