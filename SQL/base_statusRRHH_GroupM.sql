-- Drop table

DROP TABLE IF EXISTS statusRRHH;

CREATE TABLE statusRRHH (
	ID SERIAL PRIMARY KEY, 
	Miembro_del_equipo VARCHAR(300),
	Area VARCHAR(300),
	Edad numeric(50,4),
	Fecha_ingreso DATE,
	Fecha_Actual DATE,
	"Tiempo_Trabajo_en_empresa_(MESES)" numeric(50,4),
	"Experiencia Laboral total (AÑOS)" numeric(50,4),
	"Años_laborales_rubro (MARKETING DIGITAL)" numeric(50,4),
	Categorizacion VARCHAR(300),
	intro_extro VARCHAR(300),
	Energia VARCHAR(300),
	Naturaleza VARCHAR(300),
	Tácticas VARCHAR(300),
	Estudios VARCHAR(300),
	"Rubro profesional" VARCHAR(300),
	"CI TEST" numeric(50,4),
	"TIEMPO TOTAL (min)" TIME,
	"TOTAL PREGUNTAS" numeric(50,4),
	ACIERTOS numeric(50,4),
	FALLOS numeric(50,4),
	"PAREJAS NO ENCONTRADAS" numeric(50,4),
	"% EFECTIVIDAD" numeric(50,4),
	"% GLOBAL" numeric(50,4),
	Fortalezas VARCHAR(2000),
	Oportunidades VARCHAR(2000),
	Debilidades VARCHAR(2000),
	Amenazas VARCHAR(2000),
	Motivación VARCHAR(2000),
	Comentarios VARCHAR(2000)
);