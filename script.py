from googlesearch import search

keywords = [
    # Français                       Anglais
    "Sécurité de l'Active Directory", "Active Directory Security",
    "Gestion des accès",             "Access Management",
    "Contrôle d'accès",             "Access Control",
    "Identification et authentification", "Identification and Authentication",
    "Gestion des privilèges", "Privilege Management",
    "Audit de l'Active Directory", "Active Directory Auditing",
    "Protection contre les menaces internes", "Protection Against Internal Threats",
    "Protection contre les menaces externes", "Protection Against External Threats",
    "Gestion des utilisateurs", "User Management",
    "Politiques de sécurité", "Security Policies",
    "Protection des mots de passe", "Password Protection",
    "Contrôle des groupes", "Group Control",
    "Surveillance de l'Active Directory", "Active Directory Monitoring",
    "Protection des données sensibles", "Sensitive Data Protection",
    "Sécurité des groupes de sécurité", "Security Group Security",
    "Détection des anomalies", "Anomaly Detection",
    "Sauvegarde et récupération de l'Active Directory", "Active Directory Backup and Recovery",
    "Gestion des certificats", "Certificate Management",
    "Protection des comptes privilégiés", "Privileged Account Protection",
    "Authentification à deux facteurs", "Two-Factor Authentication",
    "Gestion des logs de sécurité", "Security Log Management",
    "Mise à jour de sécurité de l'Active Directory", "Active Directory Security Updates",
    "Sécurité des objets de l'Active Directory", "Active Directory Object Security",
    "Formation à la sécurité de l'Active Directory", "Active Directory Security Training",
    "Gestion des menaces internes", "Internal Threat Management",
    "Gestion des menaces externes", "External Threat Management",
    "Sécurité des serveurs Windows", "Windows Server Security",
    "Sécurité réseau", "Network Security",
    "Sécurité informatique", "Information Security",
    "Gestion des vulnérabilités", "Vulnerability Management",
    "Analyse des journaux d'activité", "Log Analysis",
    "Stratégies de sécurité", "Security Strategies",
    "Gestion des comptes d'utilisateur", "User Account Management",
    "Détection des intrusions", "Intrusion Detection",
    "Sécurité des systèmes d'exploitation Windows", "Windows OS Security",
    "Cryptographie", "Cryptography",
    "Sécurité des applications", "Application Security",
    "Gestion des correctifs", "Patch Management",
    "Sécurité des services de domaine", "Domain Services Security",
    "Mise en quarantaine des dispositifs", "Device Quarantine",
    "Sécurité des postes de travail", "Workstation Security",
    "Sécurité des serveurs", "Server Security",
    "Rétrogradation de privilèges", "Privilege De-Escalation",
    "Contrôle d'accès basé sur les rôles", "Role-Based Access Control",
    "Détection des activités suspectes", "Suspicious Activity Detection",
    "Sécurité des données Active Directory", "Active Directory Data Security",
    "Sécurité réseau Active Directory", "Active Directory Network Security",
    "Gestion des politiques de groupe", "Group Policy Management",
    "Protection des informations sensibles", "Sensitive Information Protection",
    "Sécurité des annuaires LDAP", "LDAP Directory Security",
    "Sécurité des comptes de service", "Service Account Security",
    "Sécurité des connexions RDP", "RDP Connection Security",
    "Sécurité du protocole Kerberos", "Kerberos Protocol Security",
    "Analyse comportementale des utilisateurs", "User Behavioral Analysis",
    "Sécurité des sauvegardes", "Backup Security",
    "Plan de continuité d'activité", "Business Continuity Planning",
    "Sécurité des serveurs DNS", "DNS Server Security",
    "Sécurité des réplications Active Directory", "Active Directory Replication Security",
    "Cryptage des données en transit", "Data Encryption in Transit",
    "Gestion des groupes de travail", "Workgroup Management",
    "Sécurité des stratégies de mot de passe", "Password Policy Security",
    "Sécurité du protocole NTLM", "NTLM Protocol Security",
    "Sécurité des services de certificats", "Certificate Services Security",
    "Gestion des clés de chiffrement", "Encryption Key Management",
    "Sécurité des audits Windows", "Windows Auditing Security",
    "Protection des domaines de forêt", "Forest Domain Protection",
    "Sécurité des sites Active Directory", "Active Directory Site Security",
    "Gestion des comptes d'administrateur", "Administrator Account Management",
    "Sécurité des services AD DS", "AD DS Security",
    "Sécurité des services AD LDS", "AD LDS Security",
    "Sécurité des services AD CS", "AD CS Security",
    "Sécurité des services AD RMS", "AD RMS Security",
    "Sécurité des services AD FS", "AD FS Security",
    "Sécurité des services AD CA", "AD CA Security",
]

num_results = 10

for keyword in keywords:
    print(f"Recherche de {keyword}...")

    for result in search(keyword, num_results=num_results):
        print(result)

        # insert into file
        with open("urls.txt", "a") as f:
            f.write(result + "\n")
            
    print()
