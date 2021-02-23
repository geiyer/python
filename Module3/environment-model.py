from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2, ECS
from diagrams.aws.network import ELB, Route53
from diagrams.aws.database import RDS

graph_attr = {
    "fontsize": "45",
    "bgcolor": "white"
}


with Diagram("Environment-Model", show = False, graph_attr= graph_attr):
    with Cluster("Production"):
        dns = Route53("DNS")
        lb = ELB("Load Balancer")
        with Cluster("Web Cluster"):
            web1 = EC2("Server 1")
            web2 = EC2("Server 2")
        with Cluster("Database Cluster"):
            db_master = RDS("Master")
            db_master - [RDS("Mirror 1"),
                         RDS("Mirror 2")]
        dns >> lb 
        lb >> web1 >> db_master

    with Cluster("Beta Testing"):
        dns = Route53("DNS")
        lb = ELB("Load Balancer")
        with Cluster("Web Cluster"):
            web1 = EC2("Server 1")
            web2 = EC2("Server 2")
        with Cluster("Database Cluster"):
            db_master = RDS("Master")
            db_master - [RDS("Mirror 1"),
                         RDS("Mirror 2")]
        dns >> lb 
        lb >> web1 >> db_master
    with Cluster("Quality Assurance"): 
        EC2("Web Server") >> RDS("Database")    
    with Cluster("Development"): 
        EC2("Web Server") >> RDS("Database") 
    

        
    