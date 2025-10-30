import pytest
from datetime import datetime


@pytest.mark.asyncio
async def test_get_category_empty_db(get_client):
    async with get_client as ac:
        response = await ac.get('/1')
        assert response.status_code == 404
 
@pytest.mark.parametrize(
    'name, type, expected_status',
    [
        ('name', 'type', 200),
        ('name', 'type', 400),
        
    ]
)
@pytest.mark.asyncio
async def test_add_category(get_client, name, type, expected_status): 
    async with get_client as ac:
        response = await ac.post('/categories', json={
            'name': name,
            'type': type,
            'created_at': f'{datetime.now()}',
        })
        assert response.status_code == expected_status
        
        
@pytest.mark.asyncio
async def test_get_category(get_client):
    async with get_client as ac:
        response = await ac.post('/categories', json={
            'name': 'name1',
            'type': 'type1',
            'created_at': f'{datetime.now()}',
        })
        result = await ac.get('/categories/1')
        data = result.json()
        assert data['data']['name'] == 'name'
        