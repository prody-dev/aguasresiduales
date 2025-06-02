insert campo_preservador (nombre) values 
('Hielo'),
('H2SO4'),
('HCI'),
('HNO3 SUPRAPURO'),
('K2Cr2)7 5%'),
('NaOH'),
('HNO3'),
('Otro (describir en observaciones)'),
('No Aplica');

insert campo_matriz (codigo, nombre) values 
('S', 'Solido'),
('L', 'Liquido'),
('G', 'Gaseoso'),
('O', 'Otro (describir en observaciones)');

insert campo_clave (codigo, nombre) VALUES
('AR', 'Agua Residual'),
('AP', 'Agua Potable'),
('EM', 'Emisiones'),
('AL', 'Ambiente Laboral'),
('OT', 'Otro (describir en observaciones)');

insert campo_contenedor (codigo, nombre) VALUES
('V', 'Vidrio claro'),
('F', 'Filtro'),
('A', 'Vidrio ambar'),
('B', 'Bolsa'),
('P', 'Plastico'),
('O', 'Otro (describir en observaciones)');

insert campo_tipomuestra (codigo, nombre) VALUES
('MP', 'Muestra Puntual'),
('MC', 'Muestra Compuesta');

insert campo_prioridad (codigo, descripcion) VALUES
('A', '(15) Dias habiles'),
('B', '(8-10) Dias habiles'),
('C', '(3-5) Dias habiles');

insert campo_estadocustodia (descripcion) values
('Iniciado'),
('Completado'),
('Entregado'),
('Finalizado');