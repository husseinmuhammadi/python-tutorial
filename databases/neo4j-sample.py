from langchain_neo4j import Neo4jGraph
from settings import get_settings
from database import neo4j_driver

with neo4j_driver.session() as session:
    result = session.run("MATCH (n) RETURN n LIMIT 25")
    for record in result:
        print(record)




neo4j_graph = Neo4jGraph(
    url=get_settings().NEO4J_URI,
    username=get_settings().NEO4J_USER,
    password=get_settings().NEO4J_PASSWORD,
)