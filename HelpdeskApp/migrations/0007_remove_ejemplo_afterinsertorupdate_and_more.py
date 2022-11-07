# Generated by Django 4.1.2 on 2022-11-07 21:21

from django.db import migrations
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HelpdeskApp', '0006_alter_ejemplo_edad_alter_ejemploevent_edad'),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name='ejemplo',
            name='afterinsertorupdate',
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name='ejemplo',
            name='beforedelete',
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name='ejemplo',
            name='beforeupdate',
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='ejemplo',
            trigger=pgtrigger.compiler.Trigger(name='Despues_de_Insertar_o_Actualizar', sql=pgtrigger.compiler.UpsertTriggerSql(func='INSERT INTO "HelpdeskApp_ejemploevent" ("edad", "id", "nombre", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."edad", NEW."id", NEW."nombre", _pgh_attach_context(), NOW(), \'Despues de Insertar o Actualizar\', NEW."id"); RETURN NULL;', hash='dacbf12cb0942837971be06c374e96b7d9a08b18', operation='INSERT OR UPDATE', pgid='pgtrigger_despues_de_insertar_o_actualizar_85055', table='HelpdeskApp_ejemplo', when='AFTER')),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='ejemplo',
            trigger=pgtrigger.compiler.Trigger(name='Antes_de_Eliminar', sql=pgtrigger.compiler.UpsertTriggerSql(func='INSERT INTO "HelpdeskApp_ejemploevent" ("edad", "id", "nombre", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (OLD."edad", OLD."id", OLD."nombre", _pgh_attach_context(), NOW(), \'Antes de Eliminar\', OLD."id"); RETURN NULL;', hash='ed5bf4096e975ce3b3847b70cc6d2049bdceadda', operation='DELETE', pgid='pgtrigger_antes_de_eliminar_d85a0', table='HelpdeskApp_ejemplo', when='AFTER')),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='ejemplo',
            trigger=pgtrigger.compiler.Trigger(name='Antes_de_Actualizar', sql=pgtrigger.compiler.UpsertTriggerSql(func='INSERT INTO "HelpdeskApp_ejemploevent" ("edad", "id", "nombre", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (OLD."edad", OLD."id", OLD."nombre", _pgh_attach_context(), NOW(), \'Antes de Actualizar\', OLD."id"); RETURN NULL;', hash='3cad1924f56bd54556f74a16ab63e60629f6f46d', operation='UPDATE', pgid='pgtrigger_antes_de_actualizar_372e8', table='HelpdeskApp_ejemplo', when='AFTER')),
        ),
    ]
