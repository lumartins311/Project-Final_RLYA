"""empty message

Revision ID: 4623bad8e57c
Revises: 
Create Date: 2023-09-25 17:43:58.216256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4623bad8e57c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('oficio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(length=200), nullable=True),
    sa.Column('registration_date', sa.DateTime(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('registration_date')
    )
    op.create_table('profesional',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('registration_date', sa.DateTime(), nullable=False),
    sa.Column('photo', sa.String(length=200), nullable=True),
    sa.Column('descripcion', sa.String(length=500), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('id_oficio', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_oficio'], ['oficio.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('registration_date')
    )
    op.create_table('favoritoss',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('id_prof', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_prof'], ['profesional.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tipo_consulta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_profesional', sa.Integer(), nullable=False),
    sa.Column('id_oficio', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('descripcion', sa.String(length=500), nullable=False),
    sa.Column('duracion', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['id_oficio'], ['oficio.id'], ),
    sa.ForeignKeyConstraint(['id_profesional'], ['profesional.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('consulta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('id_profesional', sa.Integer(), nullable=False),
    sa.Column('id_tipo_consulta', sa.Integer(), nullable=False),
    sa.Column('realization_date', sa.DateTime(), nullable=False),
    sa.Column('consultation_date', sa.DateTime(), nullable=False),
    sa.Column('nota', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['id_profesional'], ['profesional.id'], ),
    sa.ForeignKeyConstraint(['id_tipo_consulta'], ['tipo_consulta.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('consulta')
    op.drop_table('tipo_consulta')
    op.drop_table('favoritoss')
    op.drop_table('profesional')
    op.drop_table('user')
    op.drop_table('oficio')
    # ### end Alembic commands ###
