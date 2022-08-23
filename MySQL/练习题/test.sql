select stu.*,sc.s_score as '数学',sc2.s_score as '语文' from student as stu
inner join score as sc on sc.c_id ='01' and sc.s_id =stu.s_id
inner join score as sc2 on sc2.c_id='02' and sc2.s_id = stu.s_id
where sc.s_score > sc2.s_score;