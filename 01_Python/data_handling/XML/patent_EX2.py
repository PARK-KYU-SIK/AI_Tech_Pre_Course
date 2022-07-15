"""
<publication-reference> # 등록 관련 정보 <document-id>
<country>US</country> <doc-number>08621662</doc-number> 등록번호 <kind>B2</kind> 상태 <date>20140107</date> 등록일자 </document-id>
</publication-reference>
<application-reference appl-type="utility"> 출원 관련 정보 <document-id>
<country>US</country>
<doc-number>13175987</doc-number> 출원 번호 <date>20110705</date> 출원일
</document-id>
</application-reference>
"""
import urllib.request
from bs4 import BeautifulSoup

with open('./US08621662-20140107.xml', 'r', encoding = 'utf8') as patent_file :
    xml = patent_file.read()

soup = BeautifulSoup(xml, 'lxml')

publication_reference_tag = soup.find("publication-reference")
p_document_id_tag = publication_reference_tag.find("document-id")
p_country = p_document_id_tag.find("country").get_text()
p_doc_number = p_document_id_tag.find("doc-number").get_text()
p_kind = p_document_id_tag.find("kind").get_text()
p_date = p_document_id_tag.find("date").get_text()

application_reference_tag = soup.find("application-reference")
a_document_id_tag = publication_reference_tag.find("document-id")
a_country = p_document_id_tag.find("country").get_text()
a_doc_number = p_document_id_tag.find("doc-number").get_text()
a_date = p_document_id_tag.find("date").get_text()

print('1.','{:>9}{}'.format('p-등록국 : ',p_country))
print('2.','{:>9}{}'.format('p-등록상태 : ',p_kind))
print('3.','{:>9}{}'.format('p-등록일자 : ',p_date))
print()
print('4.','{:>9}{}'.format('a-출원국 : ',a_country))
print('5.','{:>9}{}'.format('a-등록번호 : ',a_doc_number))
print('6.','{:>9}{}'.format('a-등록일 : ',a_date))