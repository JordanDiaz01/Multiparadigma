"""empty message

Revision ID: 76eee6d76781
Revises: 
Create Date: 2023-04-16 14:19:51.892855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76eee6d76781'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('empleado',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('Puesto', sa.String(length=250), nullable=True),
    sa.Column('Sueldo', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombreProducto', sa.String(length=250), nullable=True),
    sa.Column('Costo', sa.Integer(), nullable=True),
    sa.Column('Descripcion', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Producto', sa.String(length=250), nullable=True),
    sa.Column('Costo', sa.Integer(), nullable=True),
    sa.Column('Direccion', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Menu')
    op.drop_table('Empleados')
    op.drop_table('Pedidos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Pedidos',

    )
    op.create_table('Empleados',

    )
    op.create_table('Menu',

    )
    op.drop_table('pedido')
    op.drop_table('menu')
    op.drop_table('empleado')
    # ### end Alembic commands ###
