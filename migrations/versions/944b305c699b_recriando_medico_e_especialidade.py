"""recriando medico e especialidade

Revision ID: 944b305c699b
Revises: f520c93d7279
Create Date: 2024-06-04 20:57:04.000624

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '944b305c699b'
down_revision = 'f520c93d7279'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('especialidade',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medico',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=200), nullable=True),
    sa.Column('fk_especialidade_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fk_especialidade_id'], ['especialidade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('log', schema=None) as batch_op:
        batch_op.alter_column('hash_log',
               existing_type=mysql.CHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=32),
               type_=mysql.NCHAR(national=True, length=32),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('log', schema=None) as batch_op:
        batch_op.alter_column('hash_log',
               existing_type=mysql.NCHAR(national=True, length=32),
               type_=mysql.CHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=32),
               existing_nullable=True)

    op.drop_table('medico')
    op.drop_table('especialidade')
    # ### end Alembic commands ###