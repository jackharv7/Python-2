# PyBoss

Bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:


```csv
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
```

```csv
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA

  * The `Name` column should be split into separate `First Name` and `Last Name` columns.

  * The `DOB` data should be re-written into `MM/DD/YYYY` format.

  * The `SSN` data should be re-written such that the first five numbers are hidden from view.

  * The `State` data should be re-written as simple two-letter abbreviations.

