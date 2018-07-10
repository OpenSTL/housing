from django.test import  Client
from housing.views import VacantParcels


class HomerTest(TestCase):
    def test_homer(self):
        c = Client()
        #(minPrice,maxPrice,minAcres,nbrhd,plotChoice)
        print "testing homer"
        response = c.get('/homer/',{ minPrice:'10' ,maxPrice: '1000' ,minAcres: '5' ,nbrhd:'midtown' ,plotChoice: 'prevBuild' })
        #self.assertEqual(response.status_code,200)
        self.assertTrue(False)
