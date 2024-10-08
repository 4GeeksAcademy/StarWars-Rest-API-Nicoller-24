"""empty message

Revision ID: 78756aa76050
Revises: a1ad8e29aad1
Create Date: 2024-10-04 18:52:03.687297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78756aa76050'
down_revision = 'a1ad8e29aad1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('personajes_favoritos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('personaje_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('personajes_favoritos_user_favorito_fkey', type_='foreignkey')
        batch_op.drop_constraint('personajes_favoritos_characters_favorito_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.create_foreign_key(None, 'personajes', ['personaje_id'], ['id'])
        batch_op.drop_column('characters_favorito')
        batch_op.drop_column('user_favorito')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('personajes_favoritos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_favorito', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('characters_favorito', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('personajes_favoritos_characters_favorito_fkey', 'personajes', ['characters_favorito'], ['id'])
        batch_op.create_foreign_key('personajes_favoritos_user_favorito_fkey', 'user', ['user_favorito'], ['id'])
        batch_op.drop_column('personaje_id')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
