import asyncio, time, pytest

@pytest.mark.asyncio
async def test_asyncio_concurrency_basic():
    async def work(t):
        await asyncio.sleep(t)
        return t
    t0 = time.perf_counter()
    res = await asyncio.gather(work(0.05), work(0.05))
    assert sum(res) == 0.1
    assert time.perf_counter() - t0 < 0.09  # 同時実行なら < 2 * 0.05
