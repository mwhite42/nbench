import asyncio


async def test_install(guillotina_nbench_requester):  # noqa
    async with guillotina_nbench_requester as requester:
        response, _ = await requester('GET', '/db/guillotina/@addons')
        assert 'guillotina_nbench' in response['installed']
