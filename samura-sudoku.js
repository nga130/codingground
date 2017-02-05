var load, i;
var dateID = "";

var load;
load =  "CODE:";
load +=  "SET !DATASOURCE E:/sudoku/samurai-sudoku/filename_list.csv" + "\n";
load +=  "SET !DATASOURCE_LINE {{i}}" + "\n";
load +=  "SET !EXTRACT {{!COL1}}" + "\n";

for ( i = 1; i <= 122; i++) {
    iimSet("i", i);
    iimPlay(load);
    dateID = iimGetLastExtract(0);

    iimSet("DATEID", dateID);
    iimPlay("run1.iim");
    iimPlay("run2.iim");
}
