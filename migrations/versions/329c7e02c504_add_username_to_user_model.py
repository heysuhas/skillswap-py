"""Add username to User model

Revision ID: 329c7e02c504
Revises: 
Create Date: 2025-03-25 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '329c7e02c504'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Check if the column already exists
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = [column['name'] for column in inspector.get_columns('user')]

    if 'username' not in columns:
        # Add the username column to the user table with a default value
        op.add_column('user', sa.Column('username', sa.String(length=100), nullable=False, server_default='default_username'))

        # Remove the default value constraint
        op.alter_column('user', 'username', existing_type=sa.String(length=100), nullable=False, server_default=None)
    else:
        print("Column 'username' already exists. Skipping addition.")

    # Ensure all constraints have names
    with op.batch_alter_table('match', schema=None) as batch_op:
        if not inspector.get_foreign_keys('match'):
            batch_op.create_foreign_key('fk_match_user_id', 'user', ['user_id'], ['id'])
            batch_op.create_foreign_key('fk_match_matched_with', 'user', ['matched_with'], ['id'])

def downgrade():
    # Check if the column exists before attempting to drop it
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = [column['name'] for column in inspector.get_columns('user')]

    if 'username' in columns:
        # Remove the username column from the user table
        op.drop_column('user', 'username')

    # Ensure all constraints have names
    with op.batch_alter_table('match', schema=None) as batch_op:
        if inspector.get_foreign_keys('match'):
            batch_op.drop_constraint('fk_match_user_id', type_='foreignkey')
            batch_op.drop_constraint('fk_match_matched_with', type_='foreignkey')