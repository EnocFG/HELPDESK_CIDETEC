# Generated by Django 4.1.2 on 2022-11-17 18:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="area",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_area", models.CharField(max_length=150)),
                ("codigo_area", models.CharField(max_length=10, unique=True)),
                ("descripcion", models.TextField(blank=True, null=True)),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                ("fecha_actualizacion", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="especialidad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo_especialidad", models.CharField(max_length=100)),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                ("fecha_actualizacion", models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="especialista",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_creacion", models.DateTimeField(auto_now=True)),
                ("fecha_culminacion", models.DateTimeField(null=True)),
                (
                    "especialista_especialidad",
                    models.ManyToManyField(to="HelpdeskApp.especialidad"),
                ),
            ],
            options={
                "db_table": '"HelpdeskApp_Especialista"',
            },
        ),
        migrations.CreateModel(
            name="estatus_e",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo_estatus",
                    models.CharField(
                        choices=[("1", "Activo"), ("2", "Inactivo")],
                        default="Inactivo",
                        max_length=50,
                    ),
                ),
                (
                    "fecha_creacion",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha incial"
                    ),
                ),
                ("fecha_actualizacion", models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="estatus_ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo_estatus",
                    models.CharField(
                        choices=[
                            ("1", "Creado"),
                            ("2", "Atendido"),
                            ("3", "Asignado"),
                            ("4", "Proceso"),
                            ("5", "Espera"),
                            ("6", "Resuelto"),
                            ("7", "Validado"),
                            ("8", "Cancelado"),
                            ("9", "Reasignado"),
                        ],
                        default="Creado",
                        max_length=10,
                    ),
                ),
                (
                    "fecha_creacion",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
        migrations.CreateModel(
            name="prioridad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo_prioridad",
                    models.CharField(
                        choices=[
                            ("1", "Urgente"),
                            ("2", "Alta"),
                            ("3", "Media"),
                            ("4", "Baja"),
                        ],
                        default="Urgente",
                        max_length=50,
                    ),
                ),
                (
                    "fecha_creacion",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("fecha_culminacion", models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="proyecto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_proyecto", models.CharField(max_length=150)),
                ("codigo_proyecto", models.CharField(max_length=10)),
                (
                    "fecha_inicial",
                    models.DateTimeField(null=True, verbose_name="Fecha incial"),
                ),
                (
                    "fecha_final",
                    models.DateTimeField(
                        null=True, verbose_name="Fecha final del proyecto"
                    ),
                ),
                ("descripcion", models.TextField(blank=True, null=True)),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                ("fecha_actualizacion", models.DateTimeField(auto_now=True)),
                (
                    "estatus_entidad",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HelpdeskApp.estatus_e",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="rol",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo_rol",
                    models.CharField(
                        choices=[
                            ("SA", "Super Administrador"),
                            ("GP", "Gestor proyecto"),
                            ("ES", "Especialista"),
                            ("UF", "Operador"),
                        ],
                        default="SA",
                        max_length=2,
                    ),
                ),
                ("fecha_creacion", models.DateTimeField(null=True)),
                ("fecha_actualizacion", models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo_usuario", models.CharField(max_length=20, unique=True)),
                (
                    "nombre_usuario",
                    models.TextField(max_length=150, verbose_name="Nombre usuario"),
                ),
                (
                    "apellidos_usuario",
                    models.TextField(max_length=250, verbose_name="Apellidos"),
                ),
                (
                    "email_usuario",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Correo electrónico"
                    ),
                ),
                (
                    "password",
                    models.CharField(max_length=10, verbose_name="Contraseña"),
                ),
                ("fecha_creacion", models.DateTimeField(auto_now=True)),
                ("fecha_actualizacion", models.DateTimeField(null=True)),
                (
                    "estatus_entidad",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HelpdeskApp.estatus_e",
                    ),
                ),
                (
                    "usuario_area",
                    models.ManyToManyField(to="HelpdeskApp.area", verbose_name="Área"),
                ),
                (
                    "usuario_proyecto",
                    models.ManyToManyField(
                        to="HelpdeskApp.proyecto", verbose_name="Proyecto"
                    ),
                ),
                (
                    "usuario_rol",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HelpdeskApp.rol",
                        verbose_name="Rol",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("folio", models.CharField(max_length=20, unique=True)),
                ("titulo", models.CharField(max_length=250)),
                (
                    "estatus_entidad",
                    models.CharField(
                        choices=[("draft", "Draft"), ("published", "Published")],
                        default="draft",
                        max_length=10,
                        verbose_name="Activo/Inactivo",
                    ),
                ),
                ("coordenadas", models.CharField(max_length=30, null=True)),
                (
                    "evidencias",
                    models.FileField(
                        blank=True, max_length=250, null=True, upload_to="evidencias"
                    ),
                ),
                ("descripcion", models.TextField(null=True)),
                (
                    "comentario_t",
                    models.TextField(blank=True, null=True, verbose_name="Comentario"),
                ),
                (
                    "fecha_creacion",
                    models.DateTimeField(auto_now=True, verbose_name="Fecha creacion"),
                ),
                (
                    "fecha_atendido",
                    models.DateTimeField(null=True, verbose_name="Fecha atendido"),
                ),
                (
                    "fecha_asignado",
                    models.DateTimeField(null=True, verbose_name="Fecha asignado"),
                ),
                (
                    "fecha_proceso",
                    models.DateTimeField(null=True, verbose_name="Fecha proceso"),
                ),
                (
                    "fecha_resuelto",
                    models.DateTimeField(null=True, verbose_name="Fecha resuelto"),
                ),
                (
                    "fecha_validado",
                    models.DateTimeField(null=True, verbose_name="Fecha validado"),
                ),
                (
                    "fecha_cancelado",
                    models.DateTimeField(null=True, verbose_name="Fecha cancelado"),
                ),
                ("ticket_superior", models.BigIntegerField(null=True)),
                (
                    "area_origen",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HelpdeskApp.area",
                        verbose_name="Área",
                    ),
                ),
                (
                    "especialista",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HelpdeskApp.especialista",
                        verbose_name="Especialista",
                    ),
                ),
                (
                    "estatus",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HelpdeskApp.estatus_ticket",
                        verbose_name="Status",
                    ),
                ),
                (
                    "prioridad",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HelpdeskApp.prioridad",
                        verbose_name="Prioridad",
                    ),
                ),
                (
                    "proyecto",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HelpdeskApp.proyecto",
                        verbose_name="Proyecto",
                    ),
                ),
                (
                    "usario",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HelpdeskApp.usuario",
                        verbose_name="Usuario",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="evidencia_ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("evidencia", models.BinaryField()),
                ("evidencia_ticket", models.ManyToManyField(to="HelpdeskApp.ticket")),
            ],
        ),
        migrations.AddField(
            model_name="especialista",
            name="especialista_usuario",
            field=models.ForeignKey(
                db_column="especialista_usuario",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="HelpdeskApp.usuario",
                verbose_name="especialista_u",
            ),
        ),
        migrations.AddField(
            model_name="especialista",
            name="estatus_entidad",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="HelpdeskApp.estatus_e",
            ),
        ),
        migrations.AddField(
            model_name="especialidad",
            name="proyecto_especialidad",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="HelpdeskApp.proyecto",
            ),
        ),
        migrations.CreateModel(
            name="comentario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fecha_comentario",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("contenido_ticket", models.TextField(blank=True, null=True)),
                ("status", models.BooleanField(default=True)),
                (
                    "comentario_ticket",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HelpdeskApp.ticket",
                    ),
                ),
                (
                    "comentario_usuario",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="HelpdeskApp.usuario",
                    ),
                ),
            ],
            options={
                "ordering": ("-fecha_comentario",),
            },
        ),
        migrations.AddField(
            model_name="area",
            name="area_proyecto",
            field=models.ManyToManyField(to="HelpdeskApp.proyecto"),
        ),
        migrations.AddField(
            model_name="area",
            name="estatus_entidad",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="HelpdeskApp.estatus_e",
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="usuario",
            trigger=pgtrigger.compiler.Trigger(
                name="proteger_proyecto",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func="RAISE EXCEPTION 'pgtrigger: Cannot delete rows from % table', TG_TABLE_NAME;",
                    hash="8c9d1d5584d9279588ac1453e1434361aef80469",
                    operation="DELETE",
                    pgid="pgtrigger_proteger_proyecto_4c587",
                    table="HelpdeskApp_usuario",
                    when="BEFORE",
                ),
            ),
        ),
    ]
