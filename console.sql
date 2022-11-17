---------  TRIGGER INSERT ---------------------
CREATE FUNCTION insert_status_e() RETURNS TRIGGER
AS
$$
BEGIN
INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_status_e ,tipo_estatus,fecha_creacion,fecha_actulizacion )
			               VALUES (now(), 'INSERT', user, new.id, new.tipo_estatus, new.fecha_creacion,new.fecha_actualizacion );
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION insert_status_e();

CREATE TRIGGER insert_status_e AFTER INSERT ON "HelpdeskApp_status_e"
FOR EACH ROW
EXECUTE PROCEDURE insert_status_e();

DROP TRIGGER insert_status_e on "HelpdeskApp_status_e"

SELECT * from "HelpdeskApp_status_e";
SELECT * from "HelpdeskApp_bitacora";


---------  TRIGGER DELETE ---------------------

CREATE FUNCTION delete_status_e_r() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_respaldo" (fecha, id_status_e ,tipo_estatus, fecha_creacion,fecha_actulizacion)
		                   VALUES (now(), old.id, old.tipo_estatus, old.fecha_creacion, old.fecha_actualizacion);

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_status_e_r();

CREATE TRIGGER delete_status_e_r AFTER Delete ON "HelpdeskApp_status_e"
FOR EACH ROW
EXECUTE PROCEDURE delete_status_e_r();


DROP TRIGGER delete_status_e_r on "HelpdeskApp_status_e"

---------  TRIGGER
CREATE FUNCTION delete_status_e() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_status_e ,tipo_estatus, fecha_creacion,fecha_actulizacion)
		                   VALUES (now(), 'DELETE',user, old.id, old.tipo_estatus, old.fecha_creacion, old.fecha_actualizacion);

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_status_e();

CREATE TRIGGER delete_status_e AFTER Delete ON "HelpdeskApp_status_e"
FOR EACH ROW
EXECUTE PROCEDURE delete_status_e();


DROP TRIGGER delete_status_e on "HelpdeskApp_status_e"




---------  TRIGGER UPDATE ---------------------
CREATE FUNCTION update_status_e() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_status_e ,tipo_estatus, fecha_creacion,fecha_actulizacion)
			       VALUES (now(), 'UPDATE', user, new.id, new.tipo_estatus, new.fecha_creacion,new.fecha_actualizacion);
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION update_status_e();

CREATE TRIGGER update_status_e BEFORE UPDATE ON "HelpdeskApp_status_e" FOR EACH ROW
EXECUTE PROCEDURE update_status_e();


DROP TRIGGER update_status_e on "HelpdeskApp_status_e"


---------  TRIGGER INSERT ---------------------
CREATE FUNCTION insert_proyecto() RETURNS TRIGGER
AS
$$
BEGIN
INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_status_e , id_proyecto, nombre_proyecto, codigo_proyecto, descripcion, fecha_creacion, fecha_culminacion  )
			       VALUES (now(), 'INSERT', user, new.status_entidad_id, new.id, new.nombre_proyecto, new.codigo_proyecto, new.descripcion, new.fecha_creacion,new.fecha_culminacion );
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION insert_proyecto();

CREATE TRIGGER insert_proyecto AFTER INSERT ON "HelpdeskApp_proyecto"
FOR EACH ROW
EXECUTE PROCEDURE insert_proyecto();

DROP TRIGGER insert_proyecto on "HelpdeskApp_proyecto"

---------  TRIGGER DELETE ---------------------

CREATE FUNCTION delete_proyecto() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_status_e , id_proyecto, nombre_proyecto, codigo_proyecto, descripcion, fecha_creacion, fecha_culminacion)
		                    VALUES (now(), 'DELETE',user, old.status_entidad_id, old.id, old.nombre_proyecto, old.codigo_proyecto, old.descripcion, old.fecha_creacion, old.fecha_culminacion);

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_proyecto();

CREATE TRIGGER delete_proyecto AFTER Delete ON "HelpdeskApp_proyecto"
FOR EACH ROW
EXECUTE PROCEDURE delete_proyecto();

---------  TRIGGER

CREATE FUNCTION delete_proyecto_r() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_respaldo" (fecha, id_status_e , id_proyecto, nombre_proyecto, codigo_proyecto, descripcion, fecha_creacion, fecha_culminacion)
		                    VALUES (now(), old.status_entidad_id, old.id, old.nombre_proyecto, old.codigo_proyecto, old.descripcion, old.fecha_creacion, old.fecha_culminacion);

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_proyecto();

CREATE TRIGGER delete_proyecto_r AFTER Delete ON "HelpdeskApp_proyecto"
FOR EACH ROW
EXECUTE PROCEDURE delete_proyecto_r();


---------  TRIGGER UPDATE ---------------------
CREATE FUNCTION update_proyecto() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_status_e , id_proyecto, nombre_proyecto, codigo_proyecto, descripcion, fecha_creacion, fecha_culminacion)
			       VALUES (now(), 'UPDATE', user, new.status_entidad_id, new.id, new.nombre_proyecto, new.codigo_proyecto, new.descripcion, new.fecha_creacion, new.fecha_culminacion);
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION update_proyecto();

CREATE TRIGGER update_proyecto BEFORE UPDATE ON "HelpdeskApp_proyecto" FOR EACH ROW
EXECUTE PROCEDURE update_proyecto();


DROP TRIGGER update_proyecto on "HelpdeskApp_proyecto"

---------  TRIGGER INSERT ---------------------
CREATE FUNCTION insert_area() RETURNS TRIGGER
AS
$$
BEGIN
INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_status_e , id_proyecto, id_area, nombre_area, codigo_area, descripcion,fecha_creacion, fecha_actulizacion )
			       VALUES (now(), 'INSERT', user, new.status_entidad_id, new.area_proyecto_id ,new.id, new.nombre_area, new.codigo_area, new.descripcion, new.fecha_creacion, new.fecha_actualizacion );
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION insert_area();

CREATE TRIGGER insert_area AFTER INSERT ON "HelpdeskApp_area"
FOR EACH ROW
EXECUTE PROCEDURE insert_area();

DROP TRIGGER insert_area on "HelpdeskApp_area"


SELECT * from "HelpdeskApp_area";
SELECT * from "HelpdeskApp_bitacora";

---------  TRIGGER DELETE ---------------------

CREATE FUNCTION delete_area() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_status_e , id_proyecto, id_area, nombre_area, codigo_area, descripcion, fecha_creacion, fecha_actulizacion)
		VALUES (now(), 'DELETE',user, old.status_entidad_id, old.area_proyecto_id , old.id, old.nombre_area, old.codigo_area, old.descripcion, old.fecha_creacion, old.fecha_actualizacion);

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_area();

CREATE TRIGGER delete_area AFTER Delete ON "HelpdeskApp_area"
FOR EACH ROW
EXECUTE PROCEDURE delete_area();


DROP TRIGGER delete_area on "HelpdeskApp_area"


SELECT * from "HelpdeskApp_area";

SELECT * from "HelpdeskApp_bitacora";

---------  TRIGGER

CREATE FUNCTION delete_area_r() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_respaldo" (fecha, id_status_e , id_proyecto, id_area, nombre_area, codigo_area, descripcion, fecha_creacion, fecha_actulizacion)
		VALUES (now(),  old.status_entidad_id, old.area_proyecto_id , old.id, old.nombre_area, old.codigo_area, old.descripcion, old.fecha_creacion, old.fecha_actualizacion);

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_area_r();

CREATE TRIGGER delete_area_r AFTER Delete ON "HelpdeskApp_area"
FOR EACH ROW
EXECUTE PROCEDURE delete_area_r();


DROP TRIGGER delete_area_r on "HelpdeskApp_area"


SELECT * from "HelpdeskApp_area";

SELECT * from "HelpdeskApp_respaldo";

---------  TRIGGER UPDATE ---------------------
CREATE FUNCTION update_area() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_status_e , id_proyecto, id_area, nombre_area, codigo_area, descripcion, fecha_creacion, fecha_actulizacion )
			       VALUES (now(), 'UPDATE', user, new.status_entidad_id, new.area_proyecto_id ,new.id, new.nombre_area, new.codigo_area, new.descripcion, new.fecha_creacion, new.fecha_actualizacion);
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION update_area();

CREATE TRIGGER update_area BEFORE UPDATE ON "HelpdeskApp_area" FOR EACH ROW
EXECUTE PROCEDURE update_area();


DROP TRIGGER update_area on "HelpdeskApp_area"


SELECT * from "HelpdeskApp_bitacora";

---------  TRIGGER INSERT ---------------------
CREATE FUNCTION insert_rol() RETURNS TRIGGER
AS
$$
BEGIN
INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_rol, tipo_rol,fecha_creacion, fecha_culminacion  )
			       VALUES (now(), 'INSERT', user, new.id, new.tipo_rol, new.fecha_creacion, new.fecha_culminacion  );
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION insert_rol();

CREATE TRIGGER insert_rol AFTER INSERT ON "HelpdeskApp_rol"
FOR EACH ROW
EXECUTE PROCEDURE insert_rol();

DROP TRIGGER insert_rol on "HelpdeskApp_rol"

SELECT * from "HelpdeskApp_rol";
SELECT * from "HelpdeskApp_bitacora";

 ---------------------TRIGGER DELETE ---------------------

CREATE FUNCTION delete_rol() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_rol, tipo_rol, fecha_creacion, fecha_culminacion  )
		VALUES (now(), 'DELETE',user, old.id, old.tipo_rol, old.fecha_creacion, old.fecha_culminacion );

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_rol();

CREATE TRIGGER delete_rol AFTER Delete ON "HelpdeskApp_rol"
FOR EACH ROW
EXECUTE PROCEDURE delete_rol();


DROP TRIGGER delete_rol on "HelpdeskApp_rol"

---------------------TRIGGER

CREATE FUNCTION delete_rol_r() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_respaldo" (fecha, id_rol, tipo_rol, fecha_creacion, fecha_culminacion  )
		VALUES (now(),  old.id, old.tipo_rol, old.fecha_creacion, old.fecha_culminacion );

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_rol_r();

CREATE TRIGGER delete_rol_r AFTER Delete ON "HelpdeskApp_rol"
FOR EACH ROW
EXECUTE PROCEDURE delete_rol_r();


DROP TRIGGER delete_rol on "HelpdeskApp_rol"

---------  TRIGGER UPDATE ---------------------
CREATE FUNCTION update_rol() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_rol, tipo_rol, fecha_creacion, fecha_culminacion )
			       VALUES (now(), 'UPDATE', user, new.id, new.tipo_rol, new.fecha_creacion, new.fecha_culminacion );
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION update_rol();

CREATE TRIGGER update_rol BEFORE UPDATE ON "HelpdeskApp_rol" FOR EACH ROW
EXECUTE PROCEDURE update_rol();


DROP TRIGGER update_rol on "HelpdeskApp_rol"


---------  TRIGGER INSERT ---------------------
CREATE FUNCTION insert_especialidad() RETURNS TRIGGER
AS
$$
BEGIN
INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_especialidad, tipo_especialidad,proyecto_especialidad, fecha_creacion, fecha_culminacion )
			                VALUES (now(), 'INSERT', user, new.id, new.tipo_especialidad, new.proyecto_especialidad_id, new.fecha_creacion, new.fecha_culminacion );
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION insert_especialidad();

CREATE TRIGGER insert_especialidad AFTER INSERT ON "HelpdeskApp_especialidad"
FOR EACH ROW
EXECUTE PROCEDURE insert_especialidad();

DROP TRIGGER insert_especialidad on "HelpdeskApp_especialidad"

---------  TRIGGER DELETE ---------------------

CREATE FUNCTION delete_especialidad() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_especialidad, tipo_especialidad, proyecto_especialidad, fecha_creacion, fecha_culminacion )
			                VALUES (now(), 'DELETE', user, old.id, old.tipo_especialidad, old.proyecto_especialidad_id, old.fecha_creacion, old.fecha_culminacion );

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_especialidad();

CREATE TRIGGER delete_especialidad AFTER Delete ON "HelpdeskApp_especialidad"
FOR EACH ROW
EXECUTE PROCEDURE delete_especialidad();


DROP TRIGGER delete_especialidad on "HelpdeskApp_especialidad"


---------  TRIGGER

CREATE FUNCTION delete_especialidad_r() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_respaldo" (fecha,  id_especialidad, tipo_especialidad, proyecto_especialidad, fecha_creacion, fecha_culminacion )
			                VALUES (now(),  old.id, old.tipo_especialidad, old.proyecto_especialidad_id, old.fecha_creacion, old.fecha_culminacion );

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_especialidad_r();

CREATE TRIGGER delete_especialidad_r AFTER Delete ON "HelpdeskApp_especialidad"
FOR EACH ROW
EXECUTE PROCEDURE delete_especialidad_r();


DROP TRIGGER delete_especialidad_r on "HelpdeskApp_especialidad"

---------  TRIGGER UPDATE ---------------------
CREATE FUNCTION update_especialidad() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_especialidad, tipo_especialidad, proyecto_especialidad, fecha_creacion, fecha_culminacion )
			       VALUES (now(), 'UPDATE', user, new.id, new.tipo_especialidad, new.proyecto_especialidad_id, new.fecha_creacion, new.fecha_culminacion );
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION update_especialidad();

CREATE TRIGGER update_especialidad BEFORE UPDATE ON "HelpdeskApp_especialidad" FOR EACH ROW
EXECUTE PROCEDURE update_especialidad();


DROP TRIGGER update_especialidad on "HelpdeskApp_especialidad"

---------  TRIGGER INSERT ---------------------
CREATE FUNCTION insert_usuario() RETURNS TRIGGER AS
$$
BEGIN
INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_usuario, codigo_usuario, nombre_usuario, apellidos_usuario, email_usuario, password,
                    id_status_e, id_rol, id_area, id_proyecto, fecha_creacion, fecha_actulizacion )
			       VALUES (now(), 'INSERT', user, new.id, new.codigo_usuario, new.nombre_usuario, new.apellidos_usuario, new.email_usuario, new.password,
                   new.status_entidad_id, new.usuario_rol_id, new.usuario_area_id, new.usuario_proyecto_id, new.fecha_creacion, new.fecha_actulizacion );
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION insert_usuario();

CREATE TRIGGER insert_usuario AFTER INSERT ON "HelpdeskApp_usuario"
FOR EACH ROW
EXECUTE PROCEDURE insert_usuario();

DROP TRIGGER insert_usuario on "HelpdeskApp_usuario"

INSERT INTO public."HelpdeskApp_usuario"(
	id, codigo_usuario, nombre_usuario, apellidos_usuario, email_usuario, password, fecha_creacion, status_entidad_id, usuario_rol_id, usuario_area_id, usuario_proyecto_id)
	VALUES ('3', 'U3', 'IDZEL', 'MOC', 'idzel@gmail.com', '123', '2022-11-17 01:02:00', '1', '1', '1', '1');

SELECT * from "HelpdeskApp_usuario";
SELECT * from "HelpdeskApp_bitacora";


---------  TRIGGER DELETE ---------------------

CREATE FUNCTION delete_usuario() RETURNS TRIGGER AS
$$
BEGIN
INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_usuario, codigo_usuario, nombre_usuario, apellidos_usuario, email_usuario, password,
                    id_status_e, id_rol, id_area, id_proyecto, fecha_creacion, fecha_actulizacion  )
			       VALUES (now(), 'DELETE', user, old.id, old.codigo_usuario, old.nombre_usuario, old.apellidos_usuario, old.email_usuario, old.password,
                   old.status_entidad_id, old.usuario_rol_id, old.usuario_area_id, old.usuario_proyecto_id, old.fecha_creacion, old.fecha_actulizacion );
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_usuario();

CREATE TRIGGER delete_usuario AFTER Delete ON "HelpdeskApp_usuario"
FOR EACH ROW
EXECUTE PROCEDURE delete_usuario();


DROP TRIGGER delete_usuario on "HelpdeskApp_usuario"

---------  TRIGGER

CREATE FUNCTION delete_usuario_r() RETURNS TRIGGER AS
$$
BEGIN
INSERT INTO "HelpdeskApp_respaldo" (fecha, id_usuario, codigo_usuario, nombre_usuario, apellidos_usuario, email_usuario, password,
                    id_status_e, id_rol, id_area, id_proyecto, fecha_creacion, fecha_actulizacion  )
			       VALUES (now(),  old.id, old.codigo_usuario, old.nombre_usuario, old.apellidos_usuario, old.email_usuario, old.password,
                   old.status_entidad_id, old.usuario_rol_id, old.usuario_area_id, old.usuario_proyecto_id, old.fecha_creacion, old.fecha_actulizacion );
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_usuario_r();

CREATE TRIGGER delete_usuario_r AFTER Delete ON "HelpdeskApp_usuario"
FOR EACH ROW
EXECUTE PROCEDURE delete_usuario_r();


DROP TRIGGER delete_usuario on "HelpdeskApp_usuario"


DELETE FROM public."HelpdeskApp_usuario"
	WHERE id = 3;

---------  TRIGGER UPDATE ---------------------
CREATE FUNCTION update_usuario() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_usuario, codigo_usuario, nombre_usuario, apellidos_usuario, email_usuario, password,
                    id_status_e, id_rol, id_area, id_proyecto, fecha_creacion, fecha_actulizacion )
			       VALUES (now(), 'UPDATE', user, new.id, new.codigo_usuario, new.nombre_usuario, new.apellidos_usuario, new.email_usuario, new.password,
                   new.status_entidad_id, new.usuario_rol_id, new.usuario_area_id, new.usuario_proyecto_id, new.fecha_creacion, new.fecha_actulizacion );
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION update_usuario();

CREATE TRIGGER update_usuario BEFORE UPDATE ON "HelpdeskApp_usuario" FOR EACH ROW
EXECUTE PROCEDURE update_usuario();


DROP TRIGGER update_usuario on "HelpdeskApp_usuario"
---------  TRIGGER INSERT ---------------------

CREATE FUNCTION insert_prioridad() RETURNS TRIGGER
AS
$$
BEGIN
INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_prioridad ,tipo_prioridad,fecha_creacion,fecha_culminacion  )
			       VALUES (now(), 'INSERT', user, new.id, new.tipo_prioridad, new.fecha_creacion, new.fecha_culminacion);
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION insert_prioridad();

CREATE TRIGGER insert_prioridad AFTER INSERT ON "HelpdeskApp_prioridad"
FOR EACH ROW
EXECUTE PROCEDURE insert_prioridad();

DROP TRIGGER insert_prioridad on "HelpdeskApp_prioridad"

---------  TRIGGER DELETE ---------------------

CREATE FUNCTION delete_prioridad() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_prioridad ,tipo_prioridad, fecha_creacion,fecha_culminacion)
		VALUES (now(), 'DELETE',user, old.id, old.tipo_prioridad, old.fecha_creacion, old.fecha_culminacion);

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_prioridad();

CREATE TRIGGER delete_prioridad AFTER Delete ON "HelpdeskApp_prioridad"
FOR EACH ROW
EXECUTE PROCEDURE delete_prioridad();


DROP TRIGGER delete_prioridad on "HelpdeskApp_prioridad"

---------  TRIGGER

CREATE FUNCTION delete_prioridad_r() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_respaldo" (fecha, id_prioridad ,tipo_prioridad, fecha_creacion,fecha_culminacion)
		                    VALUES (now(), old.id, old.tipo_prioridad, old.fecha_creacion, old.fecha_culminacion);

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_prioridad_r();

CREATE TRIGGER delete_prioridad_r AFTER Delete ON "HelpdeskApp_prioridad"
FOR EACH ROW
EXECUTE PROCEDURE delete_prioridad_r();


DROP TRIGGER delete_prioridad on "HelpdeskApp_prioridad"



---------  TRIGGER UPDATE ---------------------
CREATE FUNCTION update_prioridad() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion, usuario, id_prioridad ,tipo_prioridad, fecha_creacion,fecha_culminacion)
			       VALUES (now(), 'UPDATE', user, new.id, new.tipo_prioridad, new.fecha_creacion, new.fecha_culminacion);
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION update_prioridad();

CREATE TRIGGER update_prioridad BEFORE UPDATE ON "HelpdeskApp_prioridad" FOR EACH ROW
EXECUTE PROCEDURE update_prioridad();


DROP TRIGGER update_prioridad on "HelpdeskApp_prioridad"

---------  TRIGGER INSERT ---------------------
CREATE FUNCTION insert_status_ticket() RETURNS TRIGGER
AS
$$
BEGIN
INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_status_ticket ,tipo_estatus, fecha_creacion)
			       VALUES (now(), 'INSERT', user, new.id, new.tipo_estatus, new.fecha_creacion);
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION insert_status_ticket();

CREATE TRIGGER insert_status_ticket AFTER INSERT ON "HelpdeskApp_status_ticket"
FOR EACH ROW
EXECUTE PROCEDURE insert_status_ticket();

DROP TRIGGER insert_status_ticket on "HelpdeskApp_status_ticket"


SELECT * from "HelpdeskApp_status_ticket";
SELECT * from "HelpdeskApp_bitacora";


---------  TRIGGER DELETE ---------------------

CREATE FUNCTION delete_status_ticket() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_status_ticket ,tipo_estatus, fecha_creacion)
			       VALUES (now(), 'DELETE', user, old.id, old.tipo_estatus, old.fecha_creacion);

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_status_ticket();

CREATE TRIGGER delete_status_ticket AFTER Delete ON "HelpdeskApp_status_ticket"
FOR EACH ROW
EXECUTE PROCEDURE delete_status_ticket();


DROP TRIGGER delete_status_ticket on "HelpdeskApp_status_ticket"


SELECT * from "HelpdeskApp_status_ticket";

DELETE FROM public."HelpdeskApp_status_ticket"
	WHERE id = 2;

SELECT * from "HelpdeskApp_bitacora";

---------  TRIGGER

CREATE FUNCTION delete_status_ticket_r() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_respaldo" (fecha, id_status_ticket ,tipo_estatus, fecha_creacion)
			       VALUES (now(), old.id, old.tipo_estatus, old.fecha_creacion);

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_status_ticket_r();

CREATE TRIGGER delete_status_ticket_r AFTER Delete ON "HelpdeskApp_status_ticket"
FOR EACH ROW
EXECUTE PROCEDURE delete_status_ticket_r();


DROP TRIGGER delete_status_ticket_r on "HelpdeskApp_status_ticket"


---------  TRIGGER UPDATE ---------------------
CREATE FUNCTION update_status_ticket() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_status_ticket ,tipo_estatus, fecha_creacion)
			       VALUES (now(), 'UPDATE', user, new.id, new.tipo_estatus, new.fecha_creacion);
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION update_status_ticket();

CREATE TRIGGER update_status_ticket BEFORE UPDATE ON "HelpdeskApp_status_ticket" FOR EACH ROW
EXECUTE PROCEDURE update_status_ticket();


DROP TRIGGER update_status_ticket on "HelpdeskApp_status_ticket"

---------  TRIGGER INSERT ---------------------
CREATE FUNCTION insert_ticket() RETURNS TRIGGER
AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_ticket,folio,titulo,status, coordenadas, evidencias, descripcion, comentario_t,ticket_superior,
					id_area, id_especialista, id_proyecto,  id_prioridad, id_status_ticket, id_usuario,
                                   publish, fecha_atendido, fecha_asignado, fecha_proceso, fecha_espera, fecha_resuelto,fecha_validado, fecha_cancelado )
			       VALUES (now(), 'INSERT', user, new.id, new.folio, new.titulo, new.status, new.coordenadas, new.evidencias, new.descripcion, new.comentario_t, new.ticket_superior,
				   new.ticket_areaorigen_id, new.ticket_especialista_id, new.ticket_proyecto_id, new.ticket_tipoprioridad_id, new.ticket_tipostatus_id, new.ticket_usario_id,
			               new.publish, new.fecha_atendido, new.fecha_asignado, new.fecha_proceso, new.fecha_espera, new.fecha_resuelto, new.fecha_validado, new.fecha_cancelado );

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION insert_ticket();

CREATE TRIGGER insert_ticket AFTER INSERT ON "HelpdeskApp_ticket"
FOR EACH ROW
EXECUTE PROCEDURE insert_ticket();

DROP TRIGGER insert_ticket ON "HelpdeskApp_ticket"


SELECT * from "HelpdeskApp_ticket";
SELECT * from "HelpdeskApp_bitacora";


---------  TRIGGER DELETE ---------------------

CREATE FUNCTION delete_ticket() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_ticket,folio,titulo,status, coordenadas, evidencias, descripcion, comentario_t,ticket_superior,
					id_area, id_especialista, id_proyecto,  id_prioridad, id_status_ticket, id_usuario,
                                   publish, fecha_atendido, fecha_asignado, fecha_proceso, fecha_espera, fecha_resuelto,fecha_validado, fecha_cancelado )
			       VALUES (now(), 'DELETE', user, old.id, old.folio, old.titulo, old.status, old.coordenadas, old.evidencias, old.descripcion, old.comentario_t, old.ticket_superior,
				   old.ticket_areaorigen_id, old.ticket_especialista_id, old.ticket_proyecto_id, old.ticket_tipoprioridad_id, old.ticket_tipostatus_id, old.ticket_usario_id,
			               old.publish, old.fecha_atendido, old.fecha_asignado, old.fecha_proceso, old.fecha_espera, old.fecha_resuelto, old.fecha_validado, old.fecha_cancelado );

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_ticket();

CREATE TRIGGER delete_ticket AFTER Delete ON "HelpdeskApp_ticket"
FOR EACH ROW
EXECUTE PROCEDURE delete_ticket();


DROP TRIGGER delete_ticket on "HelpdeskApp_ticket"

---------  TRIGGER

CREATE FUNCTION delete_ticket_r() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_respaldo" (fecha, id_ticket,folio,titulo,status, coordenadas, evidencias, descripcion, comentario_t,ticket_superior,
					id_area, id_especialista, id_proyecto,  id_prioridad, id_status_ticket, id_usuario,
                                   publish, fecha_atendido, fecha_asignado, fecha_proceso, fecha_espera, fecha_resuelto,fecha_validado, fecha_cancelado )
			       VALUES (now(), old.id, old.folio, old.titulo, old.status, old.coordenadas, old.evidencias, old.descripcion, old.comentario_t, old.ticket_superior,
				   old.ticket_areaorigen_id, old.ticket_especialista_id, old.ticket_proyecto_id, old.ticket_tipoprioridad_id, old.ticket_tipostatus_id, old.ticket_usario_id,
			               old.publish, old.fecha_atendido, old.fecha_asignado, old.fecha_proceso, old.fecha_espera, old.fecha_resuelto, old.fecha_validado, old.fecha_cancelado );

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_ticket_r();

CREATE TRIGGER delete_ticket_r AFTER Delete ON "HelpdeskApp_ticket"
FOR EACH ROW
EXECUTE PROCEDURE delete_ticket_r();


DROP TRIGGER delete_ticket_r on "HelpdeskApp_ticket"


---------  TRIGGER UPDATE ---------------------
CREATE FUNCTION update_ticket() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion,usuario, id_ticket,folio,titulo,status, coordenadas, evidencias, descripcion, comentario_t,ticket_superior,
					id_area, id_especialista, id_proyecto,  id_prioridad, id_status_ticket, id_usuario,
                                   publish, fecha_atendido, fecha_asignado, fecha_proceso, fecha_espera, fecha_resuelto,fecha_validado, fecha_cancelado )
			       VALUES (now(), 'UPDATE', user, new.id, new.folio, new.titulo, new.status, new.coordenadas, new.evidencias, new.descripcion, new.comentario_t, new.ticket_superior,
				   new.ticket_areaorigen_id, new.ticket_especialista_id, new.ticket_proyecto_id, new.ticket_tipoprioridad_id, new.ticket_tipostatus_id, new.ticket_usario_id,
			               new.publish, new.fecha_atendido, new.fecha_asignado, new.fecha_proceso, new.fecha_espera, new.fecha_resuelto, new.fecha_validado, new.fecha_cancelado );

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION update_ticket();

CREATE TRIGGER update_ticket BEFORE UPDATE ON "HelpdeskApp_ticket" FOR EACH ROW
EXECUTE PROCEDURE update_ticket();


DROP TRIGGER update_ticket on "HelpdeskApp_ticket"

Select * From "HelpdeskApp_respaldo"

---------  TRIGGER INSERT ---------------------
CREATE FUNCTION insert_comentario() RETURNS TRIGGER
AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion, usuario, id_comentario, contenido_ticket, id_ticket, id_usuario,fecha_creacion,  fecha_culminacion )
			       VALUES (now(), 'INSERT', user, new.id, new.contenido_ticket, new.comentario_ticket_id, new.comentario_usuario_id, new.fecha_creacion, new.fecha_culminacion );

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION insert_comentario();

CREATE TRIGGER insert_comentario AFTER INSERT ON "HelpdeskApp_comentario"
FOR EACH ROW
EXECUTE PROCEDURE insert_comentario();

DROP TRIGGER insert_comentario ON "HelpdeskApp_ticket"


SELECT * from "HelpdeskApp_comentario";
SELECT * from "HelpdeskApp_bitacora";

---------  TRIGGER DELETE ---------------------

CREATE FUNCTION delete_comentario() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion, usuario, id_comentario, contenido_ticket, id_ticket, id_usuario,fecha_creacion,  fecha_culminacion)
			       VALUES (now(), 'DELETE', user, old.id, old.contenido_ticket, old.comentario_ticket_id, old.comentario_usuario_id, old.fecha_creacion, old.fecha_culminacion );
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_comentario();

CREATE TRIGGER delete_comentario AFTER Delete ON "HelpdeskApp_comentario"
FOR EACH ROW
EXECUTE PROCEDURE delete_comentario();


DROP TRIGGER delete_comentario on "HelpdeskApp_comentario"
---------  TRIGGER

CREATE FUNCTION delete_comentario_r() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_respaldo" (fecha,  id_comentario, contenido_ticket, id_ticket, id_usuario,fecha_creacion,  fecha_culminacion)
			       VALUES (now(),  old.id, old.contenido_ticket, old.comentario_ticket_id, old.comentario_usuario_id, old.fecha_creacion, old.fecha_culminacion );
RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION delete_comentario();

CREATE TRIGGER delete_comentario_r AFTER Delete ON "HelpdeskApp_comentario"
FOR EACH ROW
EXECUTE PROCEDURE delete_comentario_r();


DROP TRIGGER delete_comentario_r on "HelpdeskApp_comentario"

Select * From "HelpdeskApp_respaldo"


---------  TRIGGER UPDATE ---------------------
CREATE FUNCTION update_comentario() RETURNS TRIGGER AS
$$
BEGIN

INSERT INTO "HelpdeskApp_bitacora" (fecha, accion, usuario, id_comentario, contenido_ticket, id_ticket, id_usuario,fecha_creacion,  fecha_culminacion )
			       VALUES (now(), 'UPDATE', user, new.id, new.contenido_ticket, new.comentario_ticket_id, new.comentario_usuario_id, new.fecha_creacion, new.fecha_culminacion );

RETURN NEW;
END
$$
LANGUAGE plpgsql;


DROP FUNCTION update_comentario();

CREATE TRIGGER update_comentario BEFORE UPDATE ON "HelpdeskApp_comentario" FOR EACH ROW
EXECUTE PROCEDURE update_comentario();


DROP TRIGGER update_comentario on "HelpdeskApp_comentario"


SELECT * from "HelpdeskApp_bitacora";