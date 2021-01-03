Select 
case when Occupation = 'Doctor' Then Name  End
,case when Occupation = 'Professor' Then Name Else Null End
,case when Occupation = 'Singer' Then Name  End
,case when Occupation = 'Actor' Then Name Else Null End
,case when Occupation = 'Doctor' Then Name  End
From OCCUPATIONS
Order By 
case when Occupation = 'Doctor' Then Name  End ASC
,case when Occupation = 'Professor' Then Name  End ASC
,case when Occupation = 'Singer' Then Name  End ASC
,case when Occupation = 'Actor' Then Name  End ASC
,case when Occupation = 'Doctor' Then Name  End  ASC
;
