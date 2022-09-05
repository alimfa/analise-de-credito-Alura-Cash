#Cria DataBase
	CREATE DATABASE aluracashdados_mutuarios;

#Observa dados de cada tabela e procura por inconsistencias

	SELECT * FROM dados_mutuarios;

	SELECT person_home_ownership
	FROM dados_mutuarios 
	GROUP BY person_home_ownership;

	SELECT * FROM emprestimos;

	SELECT loan_intent
	FROM emprestimos
	GROUP BY loan_intent; 

	SELECT loan_grade
	FROM emprestimos
	GROUP BY loan_grade; 

	SELECT * FROM historicos_banco;

	SELECT cb_person_default_on_file
	FROM historicos_banco
	GROUP BY cb_person_default_on_file; 

	SELECT * FROM ids;

	#Procura por IDs repetidos
	SELECT *, COUNT(person_id) 
	FROM ids 
	GROUP BY person_id 
	HAVING COUNT(person_id) > 1;

	#Identifica IDs repetidos e exclui as 4 lnhas com person_id em branco
	SELECT * FROM ids WHERE person_id = '';
	DELETE FROM ids WHERE person_id = '';

#Junta todas as tabelas em uma só
CREATE TABLE dados AS SELECT

dm.person_age,
dm.person_income,
dm.person_home_ownership,
dm.person_emp_length,
e.loan_intent,
e.loan_grade,
e.loan_amnt,
e.loan_int_rate,
e.loan_status,
e.loan_percent_income,
hb.cb_person_default_on_file,
hb.cb_person_cred_hist_length

FROM ids i

JOIN dados_mutuarios dm ON dm.person_id = i.person_id 

JOIN emprestimos e ON e.loan_id = i.loan_id 

JOIN historicos_banco hb ON hb.cb_id = i.cb_id;

SELECT * FROM dados;

