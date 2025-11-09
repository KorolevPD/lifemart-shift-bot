import asyncio
from infra.db.database import async_session_factory, init_db
from infra.db.models import User


async def create_user(tg_id: int, role: str):
    await init_db()

    async with async_session_factory() as session:
        user = User(id=tg_id, role=role)
        session.add(user)
        await session.commit()
        print(f'User with ID:{tg_id} and "{role}" role created.')


async def add_user_interactive():
    tg_id = int(input("Enter user Telegram ID: "))
    role = (input("Enter user role (admin/employee) [employee]: ").strip()
            or "employee")

    await create_user(tg_id, role)


if __name__ == "__main__":
    asyncio.run(add_user_interactive())
