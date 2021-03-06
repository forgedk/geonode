# Generated by Django 1.11.20 on 2019-04-04 08:29


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('base', '0027_auto_20170801_1228'), ('base', '0028_resourcebase_is_approved'), ('base', '0029_auto_20171114_0341'), ('base', '0030_auto_20180309_0833'), ('base', '0031_auto_20180309_0837'), ('base', '0032_auto_20180329_1844'), ('base', '0033_auto_20180330_0951'), ('base', '0034_auto_20180606_1543'), ('base', '0035_resourcebase_dirty_state'), ('base', '0036_auto_20190129_1433'), ('base', '0037_auto_20190222_1347')]

    dependencies = [
        ('base', '26_to_27'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcebase',
            name='abstract',
            field=models.TextField(blank=True, help_text='brief narrative summary of the content of the resource(s)', max_length=2000, verbose_name='abstract'),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='data_quality_statement',
            field=models.TextField(blank=True, help_text="general explanation of the data producer's knowledge about the lineage of a dataset", max_length=2000, null=True, verbose_name='data quality statement'),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='purpose',
            field=models.TextField(blank=True, help_text='summary of the intentions with which the resource(s) was developed', max_length=500, null=True, verbose_name='purpose'),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='supplemental_information',
            field=models.TextField(default='No information provided', help_text='any other descriptive information about the dataset', max_length=2000, verbose_name='supplemental information'),
        ),
        migrations.AddField(
            model_name='resourcebase',
            name='is_approved',
            field=models.BooleanField(default=True, help_text='Is this resource validated from a publisher or editor?', verbose_name='Approved'),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='language',
            field=models.CharField(choices=[('abk','Abkhazian'), ('aar','Afar'), ('afr','Afrikaans'), ('amh','Amharic'), ('ara','Arabic'), ('asm','Assamese'), ('aym','Aymara'), ('aze','Azerbaijani'), ('bak','Bashkir'), ('ben','Bengali'), ('bih','Bihari'), ('bis','Bislama'), ('bre','Breton'), ('bul','Bulgarian'), ('bel','Byelorussian'), ('cat','Catalan'), ('cos','Corsican'), ('dan','Danish'), ('dzo','Dzongkha'), ('eng','English'), ('fra','French'), ('epo','Esperanto'), ('est','Estonian'), ('fao','Faroese'), ('fij','Fijian'), ('fin','Finnish'), ('fry','Frisian'), ('glg','Gallegan'), ('ger','German'), ('gre','Greek'), ('kal','Greenlandic'), ('grn','Guarani'), ('guj','Gujarati'), ('hau','Hausa'), ('heb','Hebrew'), ('hin','Hindi'), ('hun','Hungarian'), ('ind','Indonesian'), ('ina','Interlingua (International Auxiliary language Association)'), ('iku','Inuktitut'), ('ipk','Inupiak'), ('ita','Italian'), ('jpn','Japanese'), ('kan','Kannada'), ('kas','Kashmiri'), ('kaz','Kazakh'), ('khm','Khmer'), ('kin','Kinyarwanda'), ('kir','Kirghiz'), ('kor','Korean'), ('kur','Kurdish'), ('oci', b"Langue d 'Oc (post 1500)"), ('lao','Lao'), ('lat','Latin'), ('lav','Latvian'), ('lin','Lingala'), ('lit','Lithuanian'), ('mlg','Malagasy'), ('mlt','Maltese'), ('mar','Marathi'), ('mol','Moldavian'), ('mon','Mongolian'), ('nau','Nauru'), ('nep','Nepali'), ('nor','Norwegian'), ('ori','Oriya'), ('orm','Oromo'), ('pan','Panjabi'), ('pol','Polish'), ('por','Portuguese'), ('pus','Pushto'), ('que','Quechua'), ('roh','Rhaeto-Romance'), ('run','Rundi'), ('rus','Russian'), ('smo','Samoan'), ('sag','Sango'), ('san','Sanskrit'), ('scr','Serbo-Croatian'), ('sna','Shona'), ('snd','Sindhi'), ('sin','Singhalese'), ('ssw','Siswant'), ('slv','Slovenian'), ('som','Somali'), ('sot','Sotho'), ('spa','Spanish'), ('sun','Sudanese'), ('swa','Swahili'), ('tgl','Tagalog'), ('tgk','Tajik'), ('tam','Tamil'), ('tat','Tatar'), ('tel','Telugu'), ('tha','Thai'), ('tir','Tigrinya'), ('tog','Tonga (Nyasa)'), ('tso','Tsonga'), ('tsn','Tswana'), ('tur','Turkish'), ('tuk','Turkmen'), ('twi','Twi'), ('uig','Uighur'), ('ukr','Ukrainian'), ('urd','Urdu'), ('uzb','Uzbek'), ('vie','Vietnamese'), ('vol','Volap\xc3\xbck'), ('wol','Wolof'), ('xho','Xhosa'), ('yid','Yiddish'), ('yor','Yoruba'), ('zha','Zhuang'), ('zul','Zulu')], default='eng', help_text='language used within the dataset', max_length=3, verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='region',
            name='bbox_x0',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='bbox_x1',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='bbox_y0',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='bbox_y1',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='bbox_x0',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='bbox_x1',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='bbox_y0',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='bbox_y1',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='bbox_x0',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='bbox_x1',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='bbox_y0',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='bbox_y1',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='srid',
            field=models.CharField(default='EPSG:4326', max_length=30),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='srid',
            field=models.CharField(default='EPSG:4326', max_length=30),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='metadata_uploaded_preserve',
            field=models.BooleanField(default=False, verbose_name='Metadata uploaded preserve'),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='thumbnail_url',
            field=models.TextField(blank=True, null=True, verbose_name='Thumbnail url'),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='tkeywords',
            field=models.ManyToManyField(blank=True, help_text='formalised word(s) or phrase(s) from a fixed thesaurus used to describe the subject (space or comma-separated', to='base.ThesaurusKeyword', verbose_name='keywords'),
        ),
        migrations.AddField(
            model_name='resourcebase',
            name='dirty_state',
            field=models.BooleanField(default=False, help_text='Security Rules Are Not Synched with GeoServer!', verbose_name='Dirty State'),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
                ('blank_target', models.BooleanField()),
                ('url', models.CharField(max_length=2000)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Menu')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MenuPlaceholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='placeholder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.MenuPlaceholder'),
        ),
        migrations.AlterUniqueTogether(
            name='menuitem',
            unique_together={('menu', 'order'), ('menu', 'title')},
        ),
        migrations.AlterUniqueTogether(
            name='menu',
            unique_together={('placeholder', 'order'), ('placeholder', 'title')},
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='language',
            field=models.CharField(choices=[('abk','Abkhazian'), ('aar','Afar'), ('afr','Afrikaans'), ('amh','Amharic'), ('ara','Arabic'), ('asm','Assamese'), ('aym','Aymara'), ('aze','Azerbaijani'), ('bak','Bashkir'), ('ben','Bengali'), ('bih','Bihari'), ('bis','Bislama'), ('bre','Breton'), ('bul','Bulgarian'), ('bel','Byelorussian'), ('cat','Catalan'), ('chi','Chinese'), ('cos','Corsican'), ('dan','Danish'), ('dzo','Dzongkha'), ('eng','English'), ('fra','French'), ('epo','Esperanto'), ('est','Estonian'), ('fao','Faroese'), ('fij','Fijian'), ('fin','Finnish'), ('fry','Frisian'), ('glg','Gallegan'), ('ger','German'), ('gre','Greek'), ('kal','Greenlandic'), ('grn','Guarani'), ('guj','Gujarati'), ('hau','Hausa'), ('heb','Hebrew'), ('hin','Hindi'), ('hun','Hungarian'), ('ind','Indonesian'), ('ina','Interlingua (International Auxiliary language Association)'), ('iku','Inuktitut'), ('ipk','Inupiak'), ('ita','Italian'), ('jpn','Japanese'), ('kan','Kannada'), ('kas','Kashmiri'), ('kaz','Kazakh'), ('khm','Khmer'), ('kin','Kinyarwanda'), ('kir','Kirghiz'), ('kor','Korean'), ('kur','Kurdish'), ('oci', b"Langue d 'Oc (post 1500)"), ('lao','Lao'), ('lat','Latin'), ('lav','Latvian'), ('lin','Lingala'), ('lit','Lithuanian'), ('mlg','Malagasy'), ('mlt','Maltese'), ('mar','Marathi'), ('mol','Moldavian'), ('mon','Mongolian'), ('nau','Nauru'), ('nep','Nepali'), ('nor','Norwegian'), ('ori','Oriya'), ('orm','Oromo'), ('pan','Panjabi'), ('pol','Polish'), ('por','Portuguese'), ('pus','Pushto'), ('que','Quechua'), ('roh','Rhaeto-Romance'), ('run','Rundi'), ('rus','Russian'), ('smo','Samoan'), ('sag','Sango'), ('san','Sanskrit'), ('scr','Serbo-Croatian'), ('sna','Shona'), ('snd','Sindhi'), ('sin','Singhalese'), ('ssw','Siswant'), ('slv','Slovenian'), ('som','Somali'), ('sot','Sotho'), ('spa','Spanish'), ('sun','Sudanese'), ('swa','Swahili'), ('tgl','Tagalog'), ('tgk','Tajik'), ('tam','Tamil'), ('tat','Tatar'), ('tel','Telugu'), ('tha','Thai'), ('tir','Tigrinya'), ('tog','Tonga (Nyasa)'), ('tso','Tsonga'), ('tsn','Tswana'), ('tur','Turkish'), ('tuk','Turkmen'), ('twi','Twi'), ('uig','Uighur'), ('ukr','Ukrainian'), ('urd','Urdu'), ('uzb','Uzbek'), ('vie','Vietnamese'), ('vol','Volap\xc3\xbck'), ('wol','Wolof'), ('xho','Xhosa'), ('yid','Yiddish'), ('yor','Yoruba'), ('zha','Zhuang'), ('zul','Zulu')], default='eng', help_text='language used within the dataset', max_length=3, verbose_name='language'),
        ),
    ]
