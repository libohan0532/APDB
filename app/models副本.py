from django.db import models

# Create your models here.


class DataModel(models.Model):
    locus = models.CharField(verbose_name="编号", unique=True, primary_key=True,max_length=255)
    length = models.IntegerField(verbose_name="氨基酸数目", max_length=255)
    moltype = models.CharField(verbose_name="分子类型", max_length=255)
    topology = models.CharField(verbose_name="拓扑学形状", max_length=255)
    division = models.CharField(verbose_name="分类", max_length=255)
    update_date = models.CharField(verbose_name="更新日期", max_length=255, db_column='update-date')
    create_date = models.CharField(verbose_name="创建日期", max_length=255, db_column='create-date')
    primary_accession = models.CharField(verbose_name="初始版本号", max_length=255, db_column="primary-accession")
    accession_version = models.CharField(verbose_name="版本号", max_length=255, db_column="accession-version")
    definition = models.CharField(verbose_name="正式名称", max_length=255, db_column="definition")
    other_seqids_INSDSeqid_1 = models.CharField(verbose_name="序列编号1", max_length=255,
                                                db_column="other-seqids.INSDSeqid.1")
    other_seqids_INSDSeqid_2 = models.CharField(verbose_name="序列编号1", max_length=255,
                                                db_column="other-seqids.INSDSeqid.2")
    source = models.CharField(verbose_name="序列来源", max_length=255, db_column="source")
    organism = models.CharField(verbose_name="物种名称", max_length=255, db_column="organism")
    taxonomy = models.CharField(verbose_name="分类", max_length=255, db_column="taxonomy")

    Reference_reference_1 = models.CharField(verbose_name="参考文献1", max_length=255, db_column="Reference_reference.1")
    Reference_position_1 = models.CharField(verbose_name="对应氨基酸序列位置1", max_length=255, db_column="Reference_position.1")
    Reference_title_1 = models.CharField(verbose_name="参考文献1名称", max_length=255, db_column="Reference_title.1")
    Reference_journal_1 = models.CharField(verbose_name="参考文献期刊1", max_length=255, db_column="Reference_journal.1")

    Reference_reference_2 = models.CharField(verbose_name="参考文献2", max_length=255, db_column="Reference_reference.2")
    Reference_position_2 = models.CharField(verbose_name="对应氨基酸序列位置2", max_length=255, db_column="Reference_position.2")
    Reference_title_2 = models.CharField(verbose_name="参考文献2名称", max_length=255, db_column="Reference_title.2")
    Reference_journal_2 = models.CharField(verbose_name="参考文献期刊2", max_length=255, db_column="Reference_journal.2")

    Reference_authers_INSDAuthor_1 = models.CharField(verbose_name="作者1", max_length=255,
                                                      db_column="Reference_authers.INSDAuthor.1")
    Reference_authers_INSDAuthor_2 = models.CharField(verbose_name="作者2", max_length=255,
                                                      db_column="Reference_authers.INSDAuthor.2")
    Reference_authers_INSDAuthor_3 = models.CharField(verbose_name="作者3", max_length=255,
                                                      db_column="Reference_authers.INSDAuthor.3")
    Reference_authers_INSDAuthor_4 = models.CharField(verbose_name="作者4", max_length=255,
                                                      db_column="Reference_authers.INSDAuthor.4")
    Reference_authers_INSDAuthor_5 = models.CharField(verbose_name="作者5", max_length=255,
                                                      db_column="Reference_authers.INSDAuthor.5")
    Reference_authers_INSDAuthor_6 = models.CharField(verbose_name="作者6", max_length=255,
                                                      db_column="Reference_authers.INSDAuthor.6")

    Reference_Xref_dbname = models.CharField(verbose_name="电子期刊编码种类", max_length=255, db_column="Reference_Xref_dbname")
    Refernce_Xref_id = models.CharField(verbose_name="电子期刊编码", max_length=255, db_column="Refernce_Xref_id")
    Reference_pubmed = models.CharField(verbose_name="pubmed号码", max_length=255, db_column="Reference_pubmed")
    comment = models.CharField(verbose_name="版本号", max_length=255, db_column="comment")
    source_db = models.CharField(verbose_name="版本号", max_length=255, db_column="source-db")
    sequence = models.CharField(verbose_name="版本号", max_length=5125, db_column="sequence")

    class Meta:
        db_table = "march22data"



