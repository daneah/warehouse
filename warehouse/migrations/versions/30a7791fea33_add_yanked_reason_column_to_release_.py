# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Add yanked_reason column to Release table

Revision ID: 30a7791fea33
Revises: 43b0e796a40d
Create Date: 2020-05-09 20:25:19.454034
"""

from alembic import op
import sqlalchemy as sa


revision = '30a7791fea33'
down_revision = '43b0e796a40d'

# Note: It is VERY important to ensure that a migration does not lock for a
#       long period of time and to ensure that each individual migration does
#       not break compatibility with the *previous* version of the code base.
#       This is because the migrations will be ran automatically as part of the
#       deployment process, but while the previous version of the code is still
#       up and running. Thus backwards incompatible changes must be broken up
#       over multiple migrations inside of multiple pull requests in order to
#       phase them in over multiple deploys.

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('releases', sa.Column('yanked_reason', sa.Text(), server_default='', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('releases', 'yanked_reason')
    # ### end Alembic commands ###
