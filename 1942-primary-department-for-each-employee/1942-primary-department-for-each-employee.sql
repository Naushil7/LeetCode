SELECT 
  employee_id,
  CASE 
    WHEN COUNT(*) = 1 THEN MAX(department_id) -- If only one department, select it
    ELSE MAX(CASE WHEN primary_flag = 'Y' THEN department_id END) -- Else select the department where primary_flag is 'Y'
  END AS department_id
FROM 
  Employee
GROUP BY 
  employee_id;