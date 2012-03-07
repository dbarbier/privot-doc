#                                               -*- Makefile -*-
#
#  Makefile.am
#
#  (C) Copyright 2005-2012 EDF-EADS-Phimeca
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License.
#
#  This library is distributed in the hope that it will be useful
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
#  @author: $LastChangedBy: schueller $
#  @date:   $LastChangedDate: 2012-02-27 14:48:06 +0100 (lun. 27 févr. 2012) $
#  Id:      $Id: Makefile.am 1539 2012-02-27 13:48:06Z schueller $
#
include $(top_srcdir)/config/common.am

COMMON_SOURCES = \
        $(top_builddir)/src/GenericInformation.tex \
        $(top_srcdir)/src/logoOpenTURNS.jpg \
        docref_B11_EmpiricalCDF.tex \
        docref_B11_KernelSmoothing.tex \
        docref_B121_DistributionSelection.tex \
	docref_B122_Copulas.tex \
	docref_B122_RandomMixture.tex \
	docref_B201_Graph.tex \
	docref_B202_Smirnov.tex \
	docref_B21_MaximumLikelihood.tex \
	docref_B21_ParametricEstimation.tex \
	docref_B221_Graph.tex \
	docref_B222_BayesianInformationCriterion.tex \
	docref_B222_TestAD.tex \
	docref_B222_TestChi2.tex \
	docref_B222_TestCVM.tex \
	docref_B222_TestKS.tex \
	docref_B231_Pearson.tex \
	docref_B231_TestPearson.tex \
	docref_B232_Spearman.tex \
	docref_B232_TestSpearman.tex \
	docref_B233_TestChi2.tex \
	docref_B234_LinearRegression.tex \
	docref_C11_MinMax.tex \
	docref_C11_OptimizationAlgo.tex \
	docref_C11_ExperimentPlanes.tex \
	docref_C211_QuadraticCumul.tex \
	docref_C221_MonteCarloStd.tex \
	docref_C311_Form.tex \
	docref_C311_ReliabilityIndex.tex \
	docref_C311_Sorm.tex \
	docref_C311_TransIso_GeneralizedNataf.tex \
	docref_C311_TransIso_Rosenblatt.tex \
	docref_C311_TransIso.tex \
	docref_C312_SampleSphere.tex \
	docref_C312_StrongMaxTest.tex \
	docref_C321_MonteCarloStd.tex \
	docref_C322_DirectionalSimulation.tex \
	docref_C322_LHS.tex \
	docref_C322_QuasiMonteCarlo.tex \
	docref_C322_TI.tex \
	docref_C41_MonteCarloStd.tex \
	docref_C_DistributionRealisations.tex \
	docref_Cprime211_ImportanceFactor.tex \
	docref_Cprime212_PCC.tex \
	docref_Cprime212_Pearson.tex \
	docref_Cprime212_PRCC.tex \
	docref_Cprime212_SobolIndices.tex \
	docref_Cprime212_Spearman.tex \
	docref_Cprime212_SRC.tex \
	docref_Cprime31_ImportanceFactor.tex \
	docref_Cprime31_SensitivityFactor.tex \
	docref_SurfRep_CrossValid.tex \
	docref_SurfRep_Enum.tex \
	docref_SurfRep_FunctionalChaos.tex \
	docref_SurfRep_IntegLeastSquare.tex \
	docref_SurfRep_NumMethLS.tex \
	docref_SurfRep_LSPolynomial.tex\
	docref_SurfRep_OrthoPoly.tex \
	docref_SurfRep_PCBasis.tex \
	docref_SurfRep_PCTrunc.tex \
	docref_SurfRep_SparseLSPolynomial.tex \
	docref_SurfRep_SVR.tex \
	docref_SurfRep_Taylor.tex \
	docref_C_UniformRandomGenerator.tex \
	docref_C_LowDiscrepancySequence.tex \
	global_methodology_content.tex \
	OpenTURNS_ReferenceGuide.tex \
        reference_guide_content.tex \
        reference_guide_title.tex

COMMON_SOURCES += \
        cdf_Bernoulli.png \
        cdf_Binomial.png \
        cdf_Geometric.png \
        cdf_Poisson.png \
        cdf_UserDefined.png \
        cdf_ZipfMandelbrot_1.png \
        pdf_Arcsine.png \
        pdf_Bernoulli.png \
        pdf_Beta_1.png \
        pdf_Beta_2.png \
	pdf_Beta_3.png \
	pdf_Beta_4.png \
	pdf_Beta_5.png \
	pdf_Beta_6.png \
	pdf_Beta_7.png \
	pdf_Binomial.png \
	pdf_Burr_1.png \
	pdf_Burr_2.png \
	pdf_Burr_3.png \
	pdf_Chi_1.png \
	pdf_ChiSquare_1.png \
	pdf_ChiSquare_2.png \
	pdf_ChiSquare_3.png \
	pdf_Epanechnikov.png \
	pdf_Exponential.png \
	pdf_FisherSnedecor_1.png \
	pdf_FisherSnedecor_2.png \
	pdf_Gamma_1.png \
	pdf_Gamma_2.png \
	pdf_Gamma_3.png \
	pdf_Geometric.png \
	pdf_Gumbel.png \
	pdf_Histogram.png \
	pdf_InverseNormal_1.png \
	pdf_InverseNormal_2.png \
        pdf_Laplace.png \
        pdf_Logistic.png \
        pdf_LogNormal.png \
        pdf_LogUniform.png \
        pdf_Mixture.png \
        pdf_NonCentralChiSquare_1.png \
        pdf_NonCentralChiSquare_2.png \
	pdf_NonCentralStudent.png \
	pdf_Normal.png \
	pdf_Poisson.png \
	pdf_Rayleigh.png \
        pdf_Rice_1.png \
        pdf_Rice_2.png \
        pdf_Student.png \
        pdf_Trapezoidal.png \
        pdf_Triangular.png \
        pdf_TruncatedNormal_1.png \
        pdf_TruncatedNormal_2.png \
	pdf_TruncatedNormal_3.png \
	pdf_TruncatedNormal_4.png \
	pdf_Uniform.png \
	pdf_UserDefined.png \
	pdf_Weibull_1.png \
	pdf_Weibull_2.png \
	pdf_ZipfMandelbrot_1.png \
	qnorms_2D.png \
        RandomMixture_cdf.png \
        RandomMixture_pdf.png \
        StrongMaxTest_vicinity.png \
	enumerate.fig \
        henryBad.py \
        henry.py \
        kolmo.py \
        linearRegModel.py \
        script_henryBad.py \
        script_henry.py \
        script_pearson_test.py \
	script_QQplotDistrib.py \
	script_QQplot.py \
        script_lowDiscrepancySequences.py \
        script_spearman_test.py \
        smoothing.py

PDF_SOURCES = \
        Math_Notations.sty \
        OpenTURNS_ReferenceGuide.sty \
        AleaGauss.pdf \
        ClaytonCopula.pdf \
	enumerate.pdf \
        FigureForm.pdf \
        FigureNatafGener.pdf \
        FigureNataf.pdf \
        FigureRotationFinal.pdf \
        FigureSorm.pdf \
        FigureStrongMaxTest.pdf \
        Final_SEL_ex2_marginExp.pdf \
        flow2.pdf \
        flow3.pdf \
        flow4.pdf \
        flow5.pdf \
        flow.pdf \
        foncrep.pdf \
        FrankCopula.pdf \
        GumbelCopula.pdf \
        halton_cloud.pdf \
        henryBadGraph.pdf \
        henryGraph.pdf \
        reverseHalton_cloud.pdf \
        faure_cloud.pdf \
        haselgrove_cloud.pdf \
        IndependentCopula.pdf \
	KendallPlotCopulaBad.pdf \
	KendallPlotCopula.pdf \
	KendallPlotSample.pdf \
	KendallPlotSampleBad.pdf \
        kernelSmoothing_boundary_cdf.pdf \
        kernelSmoothing_boundary_pdf.pdf \
        kernelSmoothing_cdf.pdf \
        kernelSmoothing_pdf.pdf \
        kolmo.pdf \
        LHS_vs_MC.pdf \
        MC2.pdf \
        MC.pdf \
        mersenne_twister_cloud.pdf \
        MV.pdf \
        NormalCopula.pdf \
        OKlinearRegModel.pdf \
        OKlinearRegModelResidual.pdf \
        OKsmoothing.pdf \
        oversmoothing.pdf \
        PCE_comparisonModels.pdf \
        PCE_JacobiPolynomials_VariableE.pdf \
        PCE_JacobiPolynomials_VariableI.pdf \
        PCE_LaguerrePolynomials_VariableF.pdf \
        PCE_LegendrePolynomials_VariableL.pdf \
        pearson.pdf \
        pearson2.pdf \
        pearson3.pdf \
        plan_exp.pdf \
        QQplotBad.pdf \
        QQplotDistribBad.pdf \
        QQplotDistribOk.pdf \
        QQplotOk.pdf \
        RandomMixture_cdf.pdf \
        RandomMixture_pdf.pdf \
        Sdir.pdf \
        sobol_cloud.pdf \
        spearman.pdf \
        spearman2.pdf \
        spearman3.pdf \
        TranslatedScaledAxialGrid.pdf \
        TranslatedScaledBoxGrid.pdf \
        TranslatedScaledCompositeGrid.pdf \
        TranslatedScaledFactorialGrid.pdf \
        undersmoothing.pdf \
        WronglinearRegModel.pdf \
        WronglinearRegModelResidual.pdf

XML_SOURCES = \
        Math_Notations.plt \
        OpenTURNS_ReferenceGuide.plt \
        Arcsine.png \
        AleaGauss.png \
        ClaytonCopula.png \
	enumerate.png \
        FigureForm.png \
        FigureNatafGener.png \
        FigureNataf.png \
        FigureRotationFinal.png \
        FigureSorm.png \
        FigureStrongMaxTest.png \
        Final_SEL_ex2_marginExp.png \
        flow2.png \
        flow3.png \
        flow4.png \
        flow5.png \
        flow.png \
        foncrep.png \
        FrankCopula.png \
        GumbelCopula.png \
        halton_cloud.png \
        henryBadGraph.png \
        henryGraph.png \
        reverseHalton_cloud.png \
        faure_cloud.png \
        haselgrove_cloud.png \
        IndependentCopula.png \
	KendallPlotCopulaBad.png \
	KendallPlotCopula.png \
	KendallPlotSample.png \
	KendallPlotSampleBad.png \
        kernelSmoothing_boundary_cdf.png \
        kernelSmoothing_boundary_pdf.png \
        kernelSmoothing_cdf.png \
        kernelSmoothing_pdf.png \
        kolmo.png \
        LHS_vs_MC.png \
        MC2.png \
        MC.png \
        mersenne_twister_cloud.png \
        MV.png \
        NormalCopula.png \
        OKlinearRegModel.png \
        OKlinearRegModelResidual.png \
        OKsmoothing.png \
        oversmoothing.png \
        PCE_comparisonModels.png \
        PCE_JacobiPolynomials_VariableE.png \
        PCE_JacobiPolynomials_VariableI.png \
        PCE_LaguerrePolynomials_VariableF.png \
        PCE_LegendrePolynomials_VariableL.png \
        pearson.png \
        pearson2.png \
        pearson3.png \
        plan_exp.png \
        QQplotBad.png \
        QQplotDistribBad.png \
        QQplotDistribOk.png \
        QQplotOk.png \
        RandomMixture_cdf.png \
        RandomMixture_pdf.png \
        Sdir.png \
        sobol_cloud.png \
        spearman.png \
        spearman2.png \
        spearman3.png \
        TranslatedScaledAxialGrid.png \
        TranslatedScaledBoxGrid.png \
        TranslatedScaledCompositeGrid.png \
        TranslatedScaledFactorialGrid.png \
        Trapezoidal.png \
        undersmoothing.png \
        WronglinearRegModel.png \
        WronglinearRegModelResidual.png

# Unused:
#       Kernel_smoothing.pdf \
#
#       Kernel_smoothing.png \
# There are probably many others to remove as well

OpenTURNS_ReferenceGuide.pdf: $(COMMON_SOURCES) $(PDF_SOURCES)

OpenTURNS_ReferenceGuide.xml: $(COMMON_SOURCES) $(XML_SOURCES)

pdf-local: OpenTURNS_ReferenceGuide.pdf

doc_DATA  = OpenTURNS_ReferenceGuide.pdf
EXTRA_DIST = $(COMMON_SOURCES) $(PDF_SOURCES) 

if WITH_TRALICS
if WITH_LIBXSLT
html-local: OpenTURNS_ReferenceGuide.tgz
install-html-local: OpenTURNS_ReferenceGuide.installed
EXTRA_DIST += $(XML_SOURCES)
endif
endif
